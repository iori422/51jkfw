# -*- coding: utf-8 -*-
from  selenium import webdriver
import xlrd
import pandas as pd


fname =R"D:\2\20170418.xlsx"
bk = xlrd.open_workbook(fname)
sport = range(bk.nsheets)
try:
    sh = bk.sheet_by_name(u"成年人")
except:
    print "11111111111111111111:"+ fname

nrows = sh.nrows
ncols = sh.ncols
print "nrows %d, ncols %d" % (nrows,ncols)

for  i in range(347):
    cell_value = sh.cell_value(i,1)



