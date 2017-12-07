# -*- coding: utf-8 -*-
import MySQLdb
from  selenium import webdriver

from Script.function.Name_china import CHinaname
def sql_user():
  conn = MySQLdb.connect(
    host = 'localhost',
    port = 3306,
    user = 'root',
    passwd = '4224076w',
    db = 'test',
    charset='utf8'
     )
  name = CHinaname()
  cur = conn.cursor()
  aa = cur.execute("select checkid from `user` order by checkid DESC limit 1")
  pp = cur.fetchall()
  c=str(pp[0][0]+1)
  cur = conn.cursor()
  sqli = "insert into user values(%s,%s,%s,%s)"
  cur.execute(sqli,(c,'18011111131',name,'48'))
# cur.execute("INSERT INTO USER VALUES('20141816','18011111111','刘旺','48')")

  cur.close()
  conn.commit()
  conn.close()
  return c,name

def sql_username():
  conn = MySQLdb.connect(
    host = 'localhost',
    port = 3306,
    user = 'root',
    passwd = '4224076w',
    db = 'test',
    charset='utf8'
     )
  cur = conn.cursor()
  aa = cur.execute("select name from `user` order by checkid DESC limit 1")
  pp = cur.fetchall()
  return pp[0][0]

t=sql_username()
print t