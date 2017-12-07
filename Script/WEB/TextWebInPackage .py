# -*- coding: utf-8 -*-
import random
import urllib2,urllib
from time import sleep, time

from  selenium import webdriver
#
# from test.WEB.WEBfunction.selectDay import selectDay
# from test.function.Date import date
# from test.function.Pay import pay
import re
myprofile=webdriver.FirefoxProfile\
           (r"C:\Users\Administrator\AppData\Roaming\Mozilla\Firefox\Profiles\z13uqgmd.Test")
driver = webdriver.Firefox(myprofile)
driver.get("https://www.tijianzhuanjia.com/login.html")
driver.find_element_by_id("username").clear()
driver.find_element_by_id("username").send_keys("13111111111")
driver.find_element_by_id("password").clear()
driver.find_element_by_id("password").send_keys("111111")
driver.find_element_by_id("btn-sub").click()
# --------------------------web登录页面-------------------------------
sleep(2)
handle0 =driver.current_window_handle
print handle0

driver.find_element_by_xpath("//a[text()='体检预约']").click()
driver.find_element_by_xpath("//a[text()='查看套餐']").click()
driver.find_element_by_class_name("switch-city").click()
sleep(2)
driver.find_element_by_xpath("//div/div/a[@type='city'][4]").click()
# ----------------------------选择套餐城市----------------------------
# nowhandle =driver.current_window_handle
sleep(2)
driver.find_element_by_xpath("//div[3]/div/a[text()='查看详情']").click()
driver.close()
sleep(2)
handles =driver.window_handles
print  handles
driver.switch_to_window(handles)
driver.find_element_by_xpath("//a[text()='我要预约']").click()
# ----------------------------选择套餐--------------------------------
sleep(3)
driver.find_element_by_xpath("//div/input[@name='name']").clear()
driver.find_element_by_xpath("//div/input[@name='name']").send_keys(u"富老六")
driver.find_element_by_xpath("//div/input[@name='idCardNo']").clear()
driver.find_element_by_xpath("//div/input[@name='idCardNo']").send_keys('330101198506131417')
driver.find_element_by_xpath("//div/input[@name='mobilePhone']").clear()
driver.find_element_by_xpath("//div/input[@name='mobilePhone']").send_keys('13122222222')
driver.find_element_by_xpath("//div/input[@name='age']").clear()
driver.find_element_by_xpath("//div/input[@name='age']").send_keys('25')
driver.find_element_by_xpath("//select[@name='marriageCode']").click()
driver.find_element_by_xpath("//select/option[@value='male']").click()
sleep(2)
a= driver.find_elements_by_xpath("//button[text()='下一步']")
a[1].click()
# -----------------------------------------新增项目---------------------------------------
sleep(2)
# ---------------------------------------------------------------------------------------------
driver.find_element_by_xpath("//div[7]/button[text()='下一步']").click()
# --------------------------------------时间控件自动选择-------------------------------
sleep(2)
date(driver)
# --------------------------------------时间控件自动选择-------------------------------
driver.find_element_by_xpath("//label[@ng-if=\"dict.paymentMethodCodes.indexOf('online')>-1\"]").click()
# driver.find_element_by_xpath("//button[@validation-submit='sform']").click()
driver.find_element_by_xpath("//div[@class='gotopay']/button[@validation-submit]").click()
sleep(3)
totalpay=driver.find_element_by_xpath("/html/body/div[1]/div/section/div[2]/div/div[1]/div/p/span[2]").text
print totalpay
# https://demo.tijianzhuanjia.com/pay/index.html?p=553.72&orderNo=D12160324002&id=??? 预约订单在线支付页面
# ------------------------------------------------------------------------------------------
sleep(2)
pay(driver)
sleep(2)
driver.find_element_by_xpath("//a[@class='text-success']").click()
url = driver.current_url
print url
ddid= url[-36:]
print ddid
url = 'https://demo.tijianzhuanjia.com/order/order.json'
data = {'id':ddid,'validationCode': "1234"}
data = urllib.urlencode(data)
url2 = urllib2.Request(url,data)
respose = urllib2.urlopen(url2)
apicontent = respose.read()
print apicontent







