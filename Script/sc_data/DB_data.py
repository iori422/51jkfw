# -*- coding: utf-8 -*-
from  selenium import webdriver

from Script.function.Code import ident_generator
from Script.sql import sql_conn
def report_sc():
    cur = sql_conn().cursor()
    aa = cur.execute("select*from sc_student")
    for i in range(aa):
        pp = cur.fetchone()
        item_number = pp[0]
        item_name = pp[1]
        item_range = pp[2]
        item_unit=pp[3]
        item_value=pp[4]
        print item_number,item_name,item_range,item_unit,item_value


cur = sql_conn().cursor()
aa = cur.execute("select*from register")
for i in range(aa):
    pp = cur.fetchone()
    name = pp[0]
    sex = pp[1]
    code = pp[2]
    phone =pp[3]
    print name,sex,code,phone








