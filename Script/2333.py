# -*- coding: utf-8 -*-
from  selenium import webdriver
def web_233():
    myprofile=webdriver.FirefoxProfile\
               (r"C:\Users\Administrator\AppData\Roaming\Mozilla\Firefox\Profiles\z13uqgmd.Test")
    driver = webdriver.Firefox()
    driver.get("http://passport.233.com/login/?redirecturl=http%3A//www.233.com/")
    driver.find_element_by_xpath('//*[@id="account"]').clear()
    driver.find_element_by_xpath('//*[@id="account"]').send_keys('18075193137')
    driver.find_element_by_xpath('//*[@id="password"]').clear()
    driver.find_element_by_xpath('//*[@id="password"]').send_keys('4224076')
    driver.find_element_by_xpath('//*[@id="normalSubmit"]').click()

web_233()
