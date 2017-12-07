# -*- coding: utf-8 -*-
from time import sleep

from  selenium import webdriver
def addItems(driver):#添加自定义项目
    sleep(3)
    try :
        driver.find_element_by_xpath("//p")
        img = driver.find_elements_by_xpath("//img[@ng-src='//static-resources.tijianzhuanjia.com/wx/img/tips-close-1.gif']")
        img[1].click()
        img[0].click()
        driver.find_element_by_xpath("//div[3]/div/h3/span[text()='添加']").click()
    except:
        driver.find_element_by_xpath("//span[text()='添加']").click()
    sleep(2)
    driver.find_element_by_id("keyword").send_keys(u"糖化血红蛋白")
    driver.find_element_by_xpath("//div[text()='搜索']").click()
    sleep(1)
    driver.find_element_by_xpath("//div[4]/div/h4[@class='panel-title ng-binding']").click()

    sleep(2)
    driver.find_element_by_xpath("//li/div[text()='糖化血红蛋白测定（高效液相色谱法）']").click()
    # sleep(2)

    # Js1= "var a=document.getElementsByClassName(\"icheckbox_flat-green\")[11];a.click();"
    # driver.execute_script(Js1)
    sleep(2)
    driver.find_element_by_xpath("//button").click()
    sleep(2)
    return driver