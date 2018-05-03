#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import logging

from settings import LOG_PATH, LOG_LEVEL 
from logging.handlers import TimedRotatingFileHandler

def init_log():
    if not os.path.isdir(LOG_PATH):
        os.mkdir(LOG_PATH, 0755)
    logging.basicConfig(level=LOG_LEVEL)


class Logger(object):
    def __init__(self, log_name):
        logger = logging.getLogger(log_name)
        log_file = "{0}/{1}.log".format(LOG_PATH, log_name)

        fmt = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s', '%Y-%m-%d %H:%M:%S')

        #日志每日轮换，保存近三个月的日志
        time_handler = TimedRotatingFileHandler(log_file, when='D', interval=1, backupCount=90)
        time_handler.setFormatter(fmt)
        
        logger.addHandler(time_handler)
        
        self.logger = logger

    def info(self, msg, *args, **kwargs):
        self.logger.info(msg) 

    def debug(self, msg, *args, **kwargs):
        self.logger.debug(msg) 

    def warn(self, msg, *args, **kwargs):
        self.logger.warn(msg) 

    def error(self, msg, *args, **kwargs):
        self.logger.error(msg) 

init_log()
