#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import time
import json
from base import BaseHandler

class HomeHandler(BaseHandler):
    def handler(self, *args, **kargs):
        response = {}
        response["code"] = 200
        response["data"] = "Success"
        content = json.dumps(response)
        self.write(content)
