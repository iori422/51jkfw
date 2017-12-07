# -*- coding: utf-8 -*-
from time import sleep

from  selenium import webdriver
def Alltotal(driver):
    try:
        TJXM= driver.find_element_by_xpath("//span[@class='large ng-binding'and@ng-bind='package.discountPriceTotal']").text
    except:
        TJXM= driver.find_element_by_xpath("//div/span[2]/span[@class='large ng-binding']").text
    ZXXM= driver.find_element_by_xpath("//span[@ng-bind='customProjectsPrice | number:2']").text
    GLXM= driver.find_element_by_xpath("//span[@ng-bind='materialProjectPrice | number:2']").text
    print TJXM,ZXXM,GLXM
    total=float(TJXM)+float(ZXXM)+float(GLXM)
    print total
    print driver.find_element_by_xpath("//span[@ng-bind='totalPrice>0?(totalPrice | number:2):(-totalPrice | number:2)']").text
    if total==float(driver.find_element_by_xpath("//span[@ng-bind='totalPrice>0?(totalPrice | number:2):(-totalPrice | number:2)']").text):
        print  "价格正确"
        driver.find_element_by_xpath("//button").click()
    else:
        print "价格计算错误"
    driver.find_element_by_xpath("//button[text()='不需要修改']").click()
    sleep(2)