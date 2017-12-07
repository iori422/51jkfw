# -*- coding: utf-8 -*-
from  selenium import webdriver
def round_up(value):
      """四舍五入保留2位小数
      :param value:数值
      :return:四舍五入后的值
      """
      # 替换内置round函数,实现保留2位小数的精确四舍五入
      return round(value * 100) / 10


def anjingxinlv_jisuan():
    K= 1
    x= 72 # 心率
    age = 44
    a = 207-0.7*age
    chubei = a-x #储备心率
    fudong = chubei*0.65
    Dyundongxinlv =round(x+fudong)#运动最低心率
    Gyundongxinlv =round(x+fudong+5) #运动最高心率


    print Dyundongxinlv , Gyundongxinlv
    return [Dyundongxinlv,Gyundongxinlv]

#anjingxinlv_jisuan()

def xinlv_jisuan():
    age = 19
    a = 207-0.7*age #最大心率
    Dyundongxinlv = round(a*0.64)
    Gyundongxinlv = round(a*0.64+5)
    print Dyundongxinlv , Gyundongxinlv
    return [Dyundongxinlv,Gyundongxinlv]
xinlv_jisuan()








def kaluli_jisuan():
    sex= 1
    over = 0
    strength= 4
    if sex==0:
        x = 1.55 # 身高
        y = 70 # 体重
        a = (x*100-100)*0.9#标准体重
        print a
        BMI =round_up( y/(x*x)*0.1)
        print BMI
        if BMI <= 18.4and strength == 4:
            kcsl = 40
            over = kcsl*a
            print "消瘦"
        if  BMI> 18.5 and BMI < 23.9 and strength == 4:
            kcsl = 35
            over = kcsl*a
            print "正常"
        if  BMI>24 and strength == 4:
            kcsl = 30
            over = kcsl*a
            print "超重"
        print  over
    else:
        x = 1.43 # 身高
        y = 150 # 体重
        a = (x*100-100)*0.85#标准体重
        print a
        BMI =round_up( y/(x*x)*0.1)
        print BMI
        if BMI <= 18.4and strength == 4:
            kcsl = 45
            over = kcsl*a
            print "消瘦"
        if  BMI> 18.5 and BMI < 23.9 and strength == 4:
            kcsl = 40
            over = kcsl*a
            print "正常"
        if  BMI>24 and strength == 4:
            kcsl = 35
            over = kcsl*a
            print "超重"
        print  over

#kaluli_jisuan()





















