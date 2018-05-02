#!/usr/bin/env python
# -*- coding: utf-8 -*-

import traceback
from utils.sqlconn import DBObject

class PayInfo(object):
    @property
    def get_info(self, game_code='', sdk_code='', account=''):
        try:
            with DBObject(game_code) as dbobj:
                result = dbobj.sql_query("select * from test;")
        except Exception as e:
            traceback.print_exc()

        return result 
