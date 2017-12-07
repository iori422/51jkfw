# -*- coding: utf-8 -*-
#coding=utf-8
import  MySQLdb
from Script.function.Code import ident_generator


#--------------------- 生成项目报告------------------------------------------
def sql_conn():
 conn = MySQLdb.connect(
    host = 'localhost',
    port = 3306,
    user = 'root',
    passwd = '4224076w',
    db = 'test',
    charset='utf8'
     )
 return conn
# cur = sql_conn().cursor()
# aa = cur.execute("select checkid from `user` order by checkid DESC limit 1")
# pp = cur.fetchall()
# c=str(pp[0][0]+1)
# phone = "18075193137"
# name = u"刘金山"
# age = "45"
# data = "20170314"
# p ="instert into user values("+c+","+phone+","+name+","+age+","+data+")"
# print p
# cur.execute("instert into user values('20170101','18075193137','刘金山','45')")
# cur.execute("create table itemList(id int,item_number,item_name,item_unit,result)")
# cur.execute("create table student(id int ,item_number varchar(20),item_name varchar(30),item_unit varchar(10))")
#
# aa = cur.execute("select*from student")
# for i in range(aa):
#  pp = cur.fetchone()
#  item_number = pp[1]
#  item_name = pp[2]
#  item_unit=pp[3]
#  result = '62'  #项目值
#  code = ident_generator()
#  sheet3_data = ["1",'TT88',u"A709","0024","0024",item_number,item_number,
#                item_name,item_unit,"0-28",u"心房",result,result,"",""]#体检检查项目表
#  for a in range(len(sheet3_data)):
#           p = sheet3_data[a]
#           print p
#--------------------- 生成项目报告------------------------------------------
#  print sheet3_data
#  sheet3_loog =  len(sheet3_data)
#  for a in  range(len(sheet3_data)):
#     p = sheet3_data[a];
#     sheet3.write(1,a,sheet3_data[a],staly_1)

