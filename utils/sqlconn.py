#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: sqlconn.py
Author: xjianfeng 
Description: 数据查询类
"""
import MySQLdb
from settings import DATABASE_CONFIG as MYSQL_DATABASES

class DBObject(object):
    DictType = 1 
    DefaultType = 0 

    def __init__(self, db_key='read', database=None):
        dbconfig = MYSQL_DATABASES[db_key]
        self.database = database
        self.connect(dbconfig)

    def connect(self, dbconfig):
        host = dbconfig.get("host")
        user = dbconfig.get("user")
        passwd = dbconfig.get('passwd')
        port = int(dbconfig.get('port',3306))
        charset = dbconfig.get('charset', 'utf8')
        timeout = dbconfig.get('connect_timeout', 10)
        database = self.database or dbconfig.get('db')
        db = MySQLdb.connect(host=host, user=user, passwd=passwd, 
                            port=port,charset=charset,connect_timeout=timeout)
        db.select_db(database)
        self.db = db

    def close(self):
        try:
            if not self.db: return
            self.db.close()
        except Exception as e:
            print e.message

    def sql_query(self, sql, *arg):
        filter_sql = sql[:6] 
        if filter_sql != "SELECT" and filter_sql != "select":
            return None
        cursor = self.db.cursor(MySQLdb.cursors.DictCursor)
        if len(arg) > 0:
            #防sql注入 
            cursor.execute(sql % arg)
        else:
            cursor.execute(sql)
        result = cursor.fetchall()
        return result

    def save(self):
        pass

    def transation(self):
        pass

    def __enter__(self):
        return self

    def __exit__(self, exception_type, exception_value, traceback):
        self.close()


if __name__ == "__main__":
    with DBObject('test_db') as dbObj:
        sql = "select * from project limit 0, 1;" 
        result = dbObj.sql_query(sql)
