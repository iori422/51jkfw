# -*- coding: utf-8 -*-
from time import sleep

from  selenium import webdriver
def  loginDemo():
    myprofile=webdriver.FirefoxProfile\
           (r"C:\Users\Administrator\AppData\Roaming\Mozilla\Firefox\Profiles\z13uqgmd.Test")
    driver = webdriver.Firefox(myprofile)
    driver.set_window_size(310,710)
    driver.get("https://demo.tijianzhuanjia.com/wx/index.html?sid=00-0#/login?m=0&state={%22name%22:%22userCenter%22,%22params%22:{}}")
    sleep(5)
    driver.find_element_by_id('username').clear()
    driver.find_element_by_id('username').send_keys('13187032707')
    sleep(1)
    driver.find_element_by_xpath("//input[@placeholder='登录密码']").send_keys("11")
    driver.find_element_by_xpath("//input[@placeholder='登录密码']").send_keys("1")
    driver.find_element_by_xpath("//input[@placeholder='登录密码']").send_keys("1")
    driver.find_element_by_xpath("//input[@placeholder='登录密码']").send_keys("1")
    driver.find_element_by_xpath("//input[@placeholder='登录密码']").send_keys("1")
    sleep(1)
    driver.find_element_by_xpath('//button').click()
    sleep(3)
    return driver