#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File: server.py
Author: xianjianfeng 
Email: yourname@email.com
"""

import tornado.web
import tornado.ioloop
import tornado.httpserver
import signal
import logging

from tornado.options import define, options
from settings import SETTINGS
from route import route_handler

define("port", default=9000, help="run --port=9000", type=int)

class Application(tornado.web.Application):
    def __init__(self):
        super(Application, self).__init__(route_handler, **SETTINGS)


def stop_server():
    tornado.ioloop.IOLoop.instance().stop()


def signal_handler():
    signal.signal(signal.SIGQUIT, stop_server)
    signal.signal(signal.SIGINT, stop_server)
    signal.signal(signal.SIGHUP, stop_server)
    signal.signal(signal.SIGTERM, stop_server)


def start_server():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application()) 
    http_server.listen(options.port)

    print "Start Serever Listen Port {port}".format(port=options.port)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    start_server()
