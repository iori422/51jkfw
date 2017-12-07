# -*- coding: utf-8 -*-
from  selenium import webdriver

# 对象库中大部分使用的是前端元素IDname和Classnanme
def menu_bar(driver):
    driver.find_element_by_xpath('//*[@id="foot_bar"]/li[1]/span[1]').click()
    return
def menu_menu1(driver):
    driver.find_element_by_xpath('//*[@id="view-main"]/div[2]/div/ul/li[1]/a').click()
    return

def order(driver):# ---微信体检预约
    driver.find_element_by_xpath("/html/body/section/div[2]/div/ul/li[1]/a").click()
    return

def customize_item(driver):# ---微信体检套餐预约
    driver.find_element_by_xpath("/html/body/section/ul/li[1]").click()
    return

def PackageCost(driver):#--套餐价格
   return driver.find_element_by_xpath("//span[@class='large ng-binding'and@ng-bind='product.discountPriceTotal||0']").text

def PackageButton(driver):#--立即预约按钮
   driver.find_element_by_xpath("//button").click()
   return

def onlinePay(driver):#--在线支付
   driver.find_element_by_xpath("//label[@class='pay-check pay-check-block ']").click()
   return

def Pay(driver):#--医院支付
   driver.find_element_by_xpath("//label[@class='pay-check pay-check-block m-t-10 ']").click()
   return

def PayButton(driver):#点击支付
    driver.find_element_by_id("pay").click()
    return

def YinLianem(driver):#银联支付价格
   return   driver.find_element_by_xpath("//em[@class='order_money']").text





