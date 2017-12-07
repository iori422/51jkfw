# -*- coding: utf-8 -*-
from time import sleep

from  selenium import webdriver

phoneno=18874782058
driver= webdriver.Firefox()
driver.get("https://demo.tijianzhuanjia.com/platform/login.html")
driver.find_element_by_id("username").send_keys("admin")
driver.find_element_by_id("password").send_keys("123456789")
driver.find_element_by_xpath("//button").click()
sleep(2)
driver.find_element_by_xpath("//li[5]/a[@class='dropdown-toggle']").click()
sleep(1)
driver.find_element_by_xpath("//li/a[text()='短信列表']").click()
driver.find_element_by_id("telephone").send_keys(phoneno)
sleep(1)
driver.find_element_by_xpath("//button[text()='查 询']").click()
print driver.find_element_by_xpath("//tbody/tr[1]/td[2]").text
