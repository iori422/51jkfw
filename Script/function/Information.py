# -*- coding: utf-8 -*-
from time import sleep
from  selenium import webdriver

from Script.function.Code import ident_generator


def information(driver):#填写预约订单信息
    driver.find_element_by_xpath('//*[@id="idCardNo"]').clear()
    code = ident_generator()
    print code
    for j in range(len(code)):
        print code[j]
        driver.find_element_by_xpath("//div[3]/div[@class='col-xs-9']/input").send_keys(code[j])
    sleep(2)
    try:
        driver.find_element_by_xpath("//input[@min]").clear()
        driver.find_element_by_xpath("//input[@min]").send_keys("25")
        driver.find_element_by_xpath("//label[2]/div").click()
# driver.find_element_by_xpath("//label[1]/div").click()
        driver.find_element_by_xpath("//button").click()
    except:
        driver.find_element_by_xpath("//button").click()
    sleep(2)
