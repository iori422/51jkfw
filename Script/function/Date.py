# -*- coding: utf-8 -*-
from time import sleep, time

from  selenium import webdriver
def date(driver):#日期控件点击事件
    driver.find_element_by_xpath("/html/body/div[1]/form/div[4]/div/div/div/button").click()
    sleep(2)
    b=driver.find_elements_by_xpath("//small[text()='可约']/parent::button")
    b[len(b)-1].click()

def date2(driver):#日期控件点击事件2（判断日期是否可选）
    a=driver.find_elements_by_xpath("//td/button[not(@disabled)]/small")
    sleep(2)
    a[1].click()


