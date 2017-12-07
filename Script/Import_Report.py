#-*- coding: utf-8 -*-
from time import sleep
from  selenium import webdriver
from Script.baogao_xsl import Report

from Script.function.Date import date


def Import_report():
    myprofile=webdriver.FirefoxProfile(r"C:\Users\Administrator\AppData\Roaming\Mozilla\Firefox\Profiles\z13uqgmd.Test")
    driver = webdriver.Firefox()
    driver.get("https:/show.tijianzhuanjia.com/platform/login.html")
    driver.find_element_by_id("username").clear()
    driver.find_element_by_id("username").send_keys("admin")
    driver.find_element_by_id("password").clear()
    driver.find_element_by_id("password").send_keys("123456789")
    driver.find_element_by_id("btn-sub").click()
    sleep(3)
    driver.get("https://demo.tijianzhuanjia.com/platform/report/import/index.html?idx=1#")
    sleep(5)
    driver.find_element_by_xpath("//input[contains(@type,'file')]").send_keys(report)
    driver.find_element_by_xpath("//*[@id='validationCode']").send_keys('1234')
    driver.find_element_by_xpath("//*[@id='form-upload']/div[3]/div/button").click()
    sleep(5)
    driver.find_element_by_xpath("//option[contains(.,'体检专家健康管理中心')]").click()
    driver.find_element_by_xpath("//*[@id='form-import']/div[6]/div/label[2]").click()
    sleep(1)
    driver.find_element_by_xpath("//*[@id='form-import']/div[7]/div/button[1]").click()
    driver.get("https://demo.tijianzhuanjia.com/platform/report/record/index.html?idx=1#")
    sleep(2)
    # driver.find_element_by_xpath("//*[@id='import-report-btn']").click()
    # sleep(5)
    # driver.find_element_by_xpath("//*[@id='execute-btn']").click()
    driver.find_element_by_xpath("//*[@id='viewport']/form/div[2]/div[2]/button").click()

    driver.delete_all_cookies()


    driver.close()


for i in range(1):
    report = Report()
    sleep(5)
    Import_report()




