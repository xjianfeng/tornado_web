#!/usr/bin/env python
# -*- coding: utf-8 -*-

from base import BaseHandler

class ConfigHandler(BaseHandler):
    def handler(self):
        self.write("configinfo handler")
