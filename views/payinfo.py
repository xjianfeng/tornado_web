#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import traceback

from base import BaseHandler
from models.payinfo import PayInfo
from utils.log import Logger

class PayInfoHandler(BaseHandler):
    def handler(self, game_code='', sdk_code='', account=''):
        payobj = PayInfo(game_code) 
        if not account:
            account = self.get_argument("roleId", "")
        try:
            cnt = payobj.get_pay_cnt(sdk_code, account)
            result = {"cnt": cnt}
        except Exception as e:
            traceback.print_exc()
        else:
            response = json.dumps(result)
            return self.write(response)

        self.set_status(500)
        self.write("server interal error")
