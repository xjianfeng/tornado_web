#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import logging

APP_NAME = "sdk_service"
APP_PATH = os.path.dirname(__file__)
LOG_PATH = os.path.join(APP_PATH, "logs")
LOG_LEVEL = logging.DEBUG

__DEBUG__ = True
SETTINGS = { "gzip": True }

DATABASE_CONFIG = {
    "read": {
        "host": "xxxxx",
        "port": "3306",
	"db": "xxxx",
        "user": "root",
        "passwd": "xxxxxx",
	"charset": "utf8",
    }
}

if __DEBUG__:
    DATABASE_CONFIG['read']['host'] = "127.0.0.1"
    DATABASE_CONFIG['read']['passwd'] = "123456"
