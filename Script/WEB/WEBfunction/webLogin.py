# -*- coding: utf-8 -*-
from  selenium import webdriver
def webLogin():
     myprofile=webdriver.FirefoxProfile\
           (r"C:\Users\Administrator\AppData\Roaming\Mozilla\Firefox\Profiles\z13uqgmd.Test")
     driver = webdriver.Firefox(myprofile)
     driver.get("https://demo.tijianzhuanjia.com/login.html")
     driver.find_element_by_id("username").clear()
     driver.find_element_by_id("username").send_keys("11111111132")
     driver.find_element_by_id("password").clear()
     driver.find_element_by_id("password").send_keys("111111")
     driver.find_element_by_id("btn-sub").click()
     return driver