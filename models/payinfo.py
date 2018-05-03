#!/usr/bin/env python
# -*- coding: utf-8 -*-

import traceback
from utils.sqlconn import DBObject

pay_cnt_sql = ('select sum(log_result) cnt from log_game_role_pay '
             'where log_user="%s" and log_sdk_code="%s";')

class PayInfo(object):
    def __init__(self, db_name=''):
        self.db = "db_%s" % db_name

    def get_pay_cnt(self, sdk_code='', account=''):
        result = {}
        try:
            with DBObject(database=self.db) as dbobj:
                dataset = dbobj.sql_query(pay_cnt_sql % (account, sdk_code))
                result = dataset[0] if dataset else {}
        except Exception as e:
            result["cnt"] = -1
            traceback.print_exc()

        cnt = result.get("cnt", 0) or 0
        if cnt and not isinstance(cnt, int): cnt = int(cnt)
        return cnt 
