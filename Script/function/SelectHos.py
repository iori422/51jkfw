# -*- coding: utf-8 -*-
from  selenium import webdriver
def SelectHos(driver):#选择地图定位信息
    driver.find_element_by_xpath("//li[text()='重庆市']").click()
    driver.find_element_by_xpath('//*[@id="view-main"]/div[3]/ul/li[3]/div/div/img').click()

def SelectPackage(driver):#
    a=driver.find_elements_by_xpath("//div/h3[@class='block-title']")
    # print a[1]
    a[1].click()
