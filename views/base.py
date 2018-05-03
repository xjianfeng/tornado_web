#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import tornado
import tornado.web
import tornado.ioloop
import traceback
from utils.thread_pool import GThreadPool
from utils.log import Logger

logger = Logger("server")

class BaseHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def get(self, *args):
        """
        args是从route正则中匹配出来的参数
        """
        GThreadPool.add_job(self._call_back, self.handler, *args)

    def _call_back(self, *args):
        try:
            func = args[0][0]
            tpargs = args[0][1:]
            func(*tpargs)
            message = "%s %s (%s)" % (self.request.method, 
                                      self.request.uri, self.request.remote_ip)
            logger.info(message)
        except:
            traceback.print_exc()
        finally:
            tornado.ioloop.IOLoop.instance().add_callback(self.finish)

    def log_info(self, message):
        logger.info(message)
