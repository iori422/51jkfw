# -*- coding: utf-8 -*-
from  selenium import webdriver
import xlrd
import xdrlib ,sys
import xlwt
from  xlutils.copy import copy
import os,xlwt,datetime
import xlwt
workbook = xlwt.Workbook()

staly_1 =xlwt.XFStyle()
font1 = xlwt.Font()
font1.name = u'宋体'
font1.bold = False
font1.colour_index = 0
staly_1.font = font1

sheet1=workbook.add_sheet(u'体检报告信息',cell_overwrite_ok=True)
sheet2=workbook.add_sheet(u'体检分科检查表',cell_overwrite_ok=True)
sheet3=workbook.add_sheet(u'体检检查项目表',cell_overwrite_ok=True)
sheet4=workbook.add_sheet(u'体检业务表',cell_overwrite_ok=True)
sheet5=workbook.add_sheet(u'体检结论表',cell_overwrite_ok=True)
sheet6=workbook.add_sheet(u'疾病诊断与阳性筛查',cell_overwrite_ok=True)

sheet1_data =[ u"序号",u"体检号",u"档案号",u"身份证",u"姓名",u"拼音首码",u"0男1女",u"出生日期",u"年龄"
             ,u"电子邮件",u"电话",u"登记日期",u"体检完成日期",u"综述",u"结论",u"建议",u"预约单号"] #体检报告信息
# sheet1_loog =  len(sheet1_data)
# for a in  range(len(sheet1_data)):
#     p = sheet1_data[a];
#     sheet1.write(0,a,sheet1_data[a],staly_1)

sheet2_data = [u"序号",u"体检号",u"科室编号",u"科室名称",u"科室类型",u"科室标准代码",u"科室小结",u"科室医生",
               u"录入日期"]#体检分科检查表
# sheet2_loog =  len(sheet2_data)
# for a in  range(len(sheet2_data)):
#     p = sheet2_data[a];
#     sheet2.write(0,a,sheet2_data[a],staly_1)

sheet3_data = [u"序号",u"体检号",u"收费项目代码",u"科室编号",u"科室标准代码",u"检查项目编号",u"检查项目标准代码",
               u"检查项目名称",u"检查项目单位",u"参考范围",u"检查结果描述",u"检验结果",u"数字结果",u"结果说明",u"排序"]#体检检查项目表
# sheet3_loog =  len(sheet3_data)
# for a in  range(len(sheet3_data)):
#     p = sheet3_data[a];
#     sheet3.write(0,a,sheet3_data[a],staly_1)

sheet4_data = [u"序号",u"体检号",u"收费项目代码",u"收费项目名称",u"科室标准代码",u"科室编码",u"检查医生名称",
               u"检查日期"]#体检业务表
# sheet4_loog =  len(sheet4_data)
# for a in  range(len(sheet4_data)):
#     p = sheet4_data[a];
#     sheet4.write(0,a,sheet4_data[a],staly_1)

sheet5_data = [u"序号",u"体检号",u"科室编号",u"科室标准代码",u"结论词标准代码",u"结论编号",u"结论名称",]#体检结论表
# sheet5_loog =  len(sheet5_data)
# for a in  range(len(sheet5_data)):
#     p = sheet5_data[a];
#     sheet4.write(0,a,sheet5_data[a],staly_1)

sheet6_data = [u"序号",u"体检号",u"疾病诊断与阳性筛查",u"描述",u"类型"]#疾病诊断与阳性筛查
# sheet6_loog =  len(sheet6_data)
# for a in  range(len(sheet6_data)):
#     p = sheet6_data[a];
#     sheet4.write(0,a,sheet6_data[a],staly_1)

sheet_data = [sheet1_data,sheet2_data,sheet3_data,sheet4_data,sheet5_data,sheet6_data,]
sheet = {sheet1,sheet2,sheet3,sheet4,sheet5,sheet6,}
# for c in range(0,5):

for i in range(len(sheet)):
        c = sheet[i]
        print c
for i  in range(len(sheet_data)):
  p  =  sheet_data[i]
  for i in range(len(p)):
    g = p[i]
    print g
    # sheet_data[i].write(0,sheet[i],staly_1)

# workbook.save('D:\\test2.xls')
