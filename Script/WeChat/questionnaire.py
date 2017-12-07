# -*- coding: utf-8 -*-
import random
from time import sleep

from  selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from test.WeChat.WeChatFunction.loginDemo import loginDemo
from test.test1 import idCreact

driver =loginDemo()
sleep(3)
driver.find_element_by_xpath("//small[text()='我的健康量表卡']").click()
sleep(3)
driver.find_element_by_xpath("//span[text()='全部类型']").click()
sleep(1)
driver.find_element_by_xpath("//li[text()='阿森斯失眠量表']").click()
sleep(1)
driver.find_element_by_xpath("//span[text()='未评估']").click()
sleep(1)
driver.find_element_by_xpath("//button[@ng-show='showOk']").click()
sleep(3)
# ---------------------------------------------------------------------------
for i in range(0,8):
    group =idCreact()
    sleep(1)
    print group[i][1]

    try:
        driver.find_element_by_id(group[i][1]).click()
    except:
        driver.find_element_by_xpath("//div[@id ='qsidlb_assens_q0005_lao019']").click()

driver.find_element_by_xpath("//button[@ng-bind='btnText']").click()
sleep(1)
driver.find_element_by_xpath("//button[@ng-click='ok($event)']").click()
