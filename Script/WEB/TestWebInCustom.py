# -*- coding: utf-8 -*-
import random
from time import sleep
from  selenium import webdriver
from twisted.mail.alias import handle

from Script.function.Code import ident_generator
from Script.function.Date import date, date2

def Custom_web():
    myprofile=webdriver.FirefoxProfile\
               (r"C:\Users\Administrator\AppData\Roaming\Mozilla\Firefox\Profiles\z13uqgmd.Test")
    driver = webdriver.Firefox()
    driver.get("https://demo.tijianzhuanjia.com/login.html")
    driver.find_element_by_id("username").clear()
    driver.find_element_by_id("username").send_keys("18011111138")
    driver.find_element_by_id("password").clear()
    driver.find_element_by_id("password").send_keys("111111")
    driver.find_element_by_id("btn-sub").click()
    # --------------------------web登录页面-------------------------------
    sleep(3)
    driver.find_element_by_xpath("//a[text()='体检预约']").click()
    driver.find_element_by_xpath("/html/body/section[2]/div/div[2]/div[1]/div/a").click()
    # 婚姻状况
    sleep(3)
    married=driver.find_element_by_xpath("//option[@value='married']")
    unmarried =driver.find_element_by_xpath("//option[@value='unmarried']")
    # 性别
    male =driver.find_element_by_xpath("//option[@value='male']")
    female =driver.find_element_by_xpath("//option[@value='female']")
#    driver.find_element_by_xpath('//*[@id="sys-modal"]/div[2]/ul/li[7]').click()
#    driver.find_element_by_xpath('//*[@id="sys-modal"]/div[2]/div/div[4]/img').click()#江苏省人民医院健康体检中心
    driver.find_element_by_xpath('//*[@id="sys-modal"]/div[2]/div/div[4]/img').click()#江苏省人民医院健康体检中心
    driver.find_element_by_xpath('//*[@id="sys-modal"]/div[2]/ul/li[4]').click()
    driver.find_element_by_xpath('//*[@id="sys-modal"]/div[2]/div/div[3]/img').click()#健康管理中心
    code =  ident_generator()
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/form/div[1]/div/div/div[2]/div[1]/div/input').clear()
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/form/div[1]/div/div/div[2]/div[1]/div/input').send_keys(code)

    driver.find_element_by_xpath("//button[@validation-submit='cform']").click()
    # # -----------------------------------------新增项目---------------------------------------
    sleep(2)
    driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/div[5]/a").click()
    sleep(3)
    driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[1]/div[1]/div[2]/form/div[1]/input").send_keys(u"血型")
    driver.find_element_by_xpath("//button[text()='搜索']").click()
    sleep(2)
    driver.find_element_by_xpath("//div[@id='items-list']/div[2]/div/h3/span").click()
    driver.find_element_by_xpath("//div[@id='items-list']/div[2]/ul/li[2]/div/div").click()
    driver.find_element_by_id("project-select").click()
    sleep(5)
    # ---------------------------------------------------------------------------------------------
    jbxm = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/div[3]/span").text
    zxxm = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/div[5]/div/span").text
    glxm = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/div[6]/span").text
    total=float(jbxm)+float(zxxm)+float(glxm)
    print total
    #print float(driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/div[7]/span[2]/span").text)
    # if total==float(driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/div[7]/span[2]/span").text):
    #     print  "价格正确"
    #     driver.find_element_by_xpath("//button[@ng-click='next();']").click()
    # else:
    #     print "价格计算错误"
    driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div[7]/button').click()
    sleep(5)
    date(driver)
    sleep(2)
    js = "document.getElementsByClassName('btn btn-large btn-warning xh-highlight').onclick "
    driver.execute_script(js)
    driver.find_element_by_xpath("//div/button[@type='submit']").click()
    sleep(3)
    driver.find_element_by_xpath('//*[@id="pay"]').click()


    # driver.find_element_by_xpath('//*[@id="hd-message"]/div[3]/button').click()
    # driver.find_element_by_xpath('//*[@id="viewport"]/div/div/div[1]/a[6]').click()
    # sleep(2)
    # driver.find_element_by_xpath('//*[@id="viewport"]/div/div/div[2]/div/div/div/div[3]/a').click()
    # sleep(1)
    # a = driver.window_handles
    # driver.switch_to_window(a[1])
    # driver.find_element_by_xpath("//button[text()='取消订单']").click()
Custom_web()




















