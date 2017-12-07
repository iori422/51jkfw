# -*- coding: utf-8 -*-
from time import sleep

from  selenium import webdriver

myprofile=webdriver.FirefoxProfile\
           (r"C:\Users\Administrator\AppData\Roaming\Mozilla\Firefox\Profiles\z13uqgmd.Test")
driver = webdriver.Firefox()

driver.get("https://demo.tijianzhuanjia.com/platform/login.html")
driver.find_element_by_id("username").send_keys("xn002")
driver.find_element_by_id("password").send_keys("111111")
driver.find_element_by_id("btn-sub").click()
sleep(3)
try:
    driver.find_element_by_xpath("//span[text()='订单管理员']")
    print "登录成功"
except:
    print "登录失败"

driver.find_element_by_xpath("//span[@class='menu-text'and text()='团检管理']").click()
sleep(1)
driver.find_element_by_xpath("//a[text()='创建团检']").click()
sleep(3)
driver.find_element_by_id("addGro"
                          "upcheck").click()
sleep(1)
driver.find_element_by_id("btn-confirm").click()
sleep(3)
try:
    driver.find_element_by_xpath("//span").click()
except:
    print "找不到元素"
# 创建团检----------------------------------------------------------------
driver.find_element_by_xpath("//input[@autocomplete='off']").send_keys(u'多多网络')
driver.find_element_by_xpath("//li[@data-option-array-index='5']").click()
driver.find_element_by_xpath("//input[@name='beginDate']").click()
driver.find_element_by_xpath("//td[@class='today day']").click()
driver.find_element_by_xpath("//button[@class='btn btn-success addperson']").click()
sleep(2)
now_handle = driver.current_window_handle
all_handle = driver.window_handles
print  now_handle,all_handle
driver.switch_to_window(all_handle[1])
driver.find_element_by_xpath("//tr[1]/td/input[@class='selected']").click()
sleep(2)
driver.find_element_by_xpath("//a[text()='安排体检']").click()
sleep(3)
driver.find_element_by_xpath("//a[@class='chosen-single']").click()
# driver.find_element_by_xpath("//a[@class='btn btn-success btn-large']").click()
# driver.find_element_by_xpath("//div[@class = 'chosen-container chosen-container-single']").click()

sleep(2)
driver.find_element_by_xpath("//ul/li[@data-option-array-index='2']").click()
driver.find_element_by_id("btn-arrangepe").click()
sleep(2)
driver.find_element_by_xpath("//button[@class='btn btn-primary']").click()
sleep(2)

all_handle = driver.window_handles
driver.switch_to_window(all_handle[0])
driver.find_element_by_xpath("//button[@id='submit']").click()
sleep(1)
driver.find_element_by_xpath("//button[@class='btn btn-warning']").click()
sleep(2)
a = driver.find_elements_by_xpath("//tr/td/a[text()='安排']")
a[0].click()
print a
# 安排团检----------------------------------------------------------------
all_handle = driver.window_handles
driver.switch_to_window(all_handle[1])
sleep(2)
driver.find_element_by_xpath("//a[text()='安排单一日期']").click()
# driver.find_element_by_xpath("//a[text()='安排范围日期']").click()
driver.find_element_by_xpath("//input[@name='physicalExaminationDate']").click()
driver.find_element_by_xpath("//tr/td[@class='today day']").click()
driver.find_element_by_xpath("//input[@name='physicalExaminationNumber']").send_keys('1')
driver.find_element_by_xpath("//button[@id='submit']").click()
sleep(1)
driver.find_element_by_xpath("//button[@class='btn btn-warning']").click()
sleep(2)
all_handle = driver.window_handles
driver.switch_to_window(all_handle[0])
driver.find_element_by_xpath("//a[text()='确定团检']").click()
sleep(2)
driver.find_element_by_xpath("//a[text()='处理']").click()
all_handle = driver.window_handles
driver.switch_to_window(all_handle[1])
sleep(2)
driver.find_element_by_xpath("//input[@type = 'checkbox']").click()
driver.find_element_by_xpath("//a[@class='btn btn-success assigndate']").click()
sleep(1)
driver.find_element_by_xpath("//button[@class='btn btn-warning']").click()
sleep(2)
driver.find_element_by_xpath("//button[@class='btn btn-primary']").click()
sleep(1)
driver.find_element_by_xpath("//button[@class='btn btn-success btn-large']").click()
sleep(1)
driver.find_element_by_xpath("//button[@class='btn btn-warning']").click()
sleep(1)
driver.find_element_by_xpath("//button[@class='btn btn-warning']").click()
print "团检订单建立成功"



