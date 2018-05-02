#!/usr/bin/env python
# -*- coding: utf-8 -*-

from base import BaseHandler

class PayInfoHandler(BaseHandler):
    def handler(self, game_code='', sdk_code=''):
        content = "game_code={0}&sdk_code={1}".format(game_code, sdk_code)
        self.write(content)
