# -*- coding: utf-8 -*-
import random
from time import sleep
from  selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
# --------------------------web登录页面-------------------------------
from test.WEB.WEBfunction.selectDay import selectDay
from test.function.Date import date

myprofile=webdriver.FirefoxProfile\
           (r"C:\Users\Administrator\AppData\Roaming\Mozilla\Firefox\Profiles\z13uqgmd.Test")
driver = webdriver.Firefox(myprofile)
driver.get("https://demo.tijianzhuanjia.com/login.html")
driver.find_element_by_id("username").clear()
driver.find_element_by_id("username").send_keys("13111111111")
driver.find_element_by_id("password").clear()
driver.find_element_by_id("password").send_keys("111111")
driver.find_element_by_id("btn-sub").click()
# --------------------------web登录页面----------------------------
# --------------------------人员信息-------------------------------
driver.implicitly_wait(60)
driver.find_element_by_xpath("//a[text()='体检预约']").click()
driver.find_element_by_xpath("//a[@class='ind-start']").click()
driver.implicitly_wait(60)
driver.find_element_by_xpath("//input[@name='name']").clear()
driver.find_element_by_xpath("//input[@name='name']").send_keys(u"木村")
driver.find_element_by_xpath("//input[@maxlength='3']").clear()
driver.find_element_by_xpath("//input[@maxlength='3']").send_keys('60')
# --------------------------web登录页面-------------------------------
#-------------------------获得select所有数据并选择--------------------
nation=[]
for i in range(57):
     i= str(i)
     vid= "//option[@value='1234']".replace('1234',i)
     nation.append(vid)
print "数据3==="+nation[3]
driver.find_element_by_xpath(nation[1]).click()
#-------------------------获得select所有数据并选择--------------------
job=random.choice(["//option[text()='无']","//option[text()='国家公务员']","//option[text()='专业技术人员']","//option[text()='职员']"])
driver.find_element_by_xpath(job).click()
driver.find_element_by_xpath("//input[@name='height']").clear()
driver.find_element_by_xpath("//input[@name='height']").send_keys('175')
driver.find_element_by_xpath("//input[@name='weight']").clear()
driver.find_element_by_xpath("//input[@name='weight']").send_keys('60')
driver.find_element_by_xpath("//div/select[@name='marriageCode']/option[1]").click()
driver.find_element_by_xpath("//button[text()='下一步']").click()
#-------------------------获得select所有数据并选择---------------------
sleep(3)
# --------------需要增加自动选择题目的功能-----------------------------
driver.find_element_by_xpath("//button[@ng-click='next()']").click()
sleep(1)
driver.find_element_by_xpath("//button[@ng-click='next()']").click()
sleep(1)
driver.find_element_by_xpath("//button[@ng-click='next()']").click()
sleep(1)
driver.find_element_by_xpath("//button[@ng-click='next()']").click()
sleep(5)
# driver.find_element_by_xpath("//button[@ng-click='next()']").click()
# sleep(5)
# driver.find_element_by_xpath("//button[text()='依据体检建议，制定体检套餐']").click()
driver.find_element_by_xpath("/html/body/div[1]/div/div[4]/button").click()
# --------------需要增加自动选择题目的功能-----------------------------
# ---------------------------------选择城市----------------------------
# city= random.choice(["//li[text()=\'成都市\']"])
city= random.choice(["//li[text()=\'重庆市\']"])
print city
sleep(3)
driver.find_element_by_xpath(city).click()
driver.find_element_by_xpath("//div[@val='00-3']").click()
sleep(3)
# ---------------------------------------选择城市----------------------------

# --------------------------------确认订单页面-------------------------------
# ------------------------------------新增项目-------------------------------
driver.find_element_by_xpath("//div[text()='基础必查套餐']").click()
sleep(5)
driver.find_element_by_xpath("//a[@ng-click='showCustom();']").click()
driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[1]/div[1]/div[2]/form/div[1]/input").send_keys(u"血型")
driver.find_element_by_xpath("//button[text()='搜索']").click()
driver.implicitly_wait(60)
# driver.find_element_by_xpath("//div[@id='items-list']/div[2]/div/h3/span").click()
driver.find_element_by_xpath("//div[@id='items-list']/div[2]/div/h3/span").click()
driver.find_element_by_xpath("//div[@id='items-list']/div[2]/ul/li[2]/div/div").click()
driver.find_element_by_id("project-select").click()
driver.implicitly_wait(60)
# ------------------------------------新增项目-------------------------------
jbxm = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/div[3]/span").text
zxxm = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/div[5]/div/span").text
glxm = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/div[6]/span").text
tjxm = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/div[4]/span").text
driver.implicitly_wait(60)
total=float(jbxm)+float(zxxm)+float(glxm)+float(tjxm)
print total
# print float(driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/div[7]/span[2]/span").text)
a=driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/div[7]/span[2]/span").text
a = float(a.replace(',',''))
if total==a:
    print  "价格正确"
    sleep(3)
    driver.find_element_by_xpath("//button[@ng-click='next();']").click()
else:
    print "价格计算错误"
sleep(3)
driver.implicitly_wait(60)
# --------------------------------确认订单页面-------------------------------
# ----------------------------身份证信息-------------------------------------------------
driver.find_element_by_xpath("//input[@name='name']").clear()
driver.find_element_by_xpath("//input[@name='name']").send_keys(u"苜蓿")
driver.find_element_by_xpath("//input[@name='mobilePhone']").clear()
driver.find_element_by_xpath("//input[@name='mobilePhone']").send_keys('11111111111')
driver.find_element_by_xpath("//input[@name='idCardNo']").clear()
driver.find_element_by_xpath("//input[@name='idCardNo']").send_keys('410103199404012078')
driver.find_element_by_xpath("/html/body/div[1]/div[2]/form/div[3]/button").click()
# ----------------------------身份证信息-------------------------------------------------
# --------------------------------------时间控件自动选择-------------------------------
sleep(2)
date(driver)
# --------------------------------------时间控件自动选择-------------------------------
driver.find_element_by_xpath("//label[@ng-if=\"dict.paymentMethodCodes.indexOf('online')>-1\"]").click()
driver.find_element_by_xpath("//button[@validation-submit='sform']").click()
driver.implicitly_wait(60)
