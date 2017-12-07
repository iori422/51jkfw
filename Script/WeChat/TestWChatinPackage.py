# -*- coding: utf-8 -*-

from time import sleep

from test.WeChat.WeChatFunction.WChatObject import menu_bar, menu_menu1, order, customize_item, PackageCost, PackageButton, onlinePay, \
    PayButton, YinLianem
from test.WeChat.WeChatFunction.WeChatLogin import login
from test.function.AddItems import addItems
from test.function.Date import date
from test.function.Information import information
from test.function.Totalall import Alltotal

driver = login()
sleep(3)
menu_bar(driver)
sleep(1)
menu_menu1(driver)
sleep(1)
order(driver)
sleep(1)
customize_item(driver)
sleep(5)
# driver.find_element_by_xpath("//span[@ng-bind-html]").click()
driver.find_element_by_xpath("//div/div[2][@class='srp-block  line-right']").click()
sleep(1)
driver.find_element_by_xpath("/html/body/section/div[1]/div[2]/ul/li[1]/div[1]/ul/li[7]").click()
sleep(1)
driver.find_element_by_xpath("//li/button[text()='确 定']").click()
sleep(1)
driver.find_element_by_xpath("//span[@ng-bind-html]").click()
sleep(1)
driver.find_element_by_xpath("//ul/li[text()='价格从低到高']").click()
sleep(1)
driver.find_element_by_id("item0").click()
sleep(2)
packt = PackageCost(driver)
print packt
PackageButton(driver)
sleep(2)
b = information(driver)
sleep(2)
addItems(driver)
sleep(1)
Alltotal(driver)
PackageButton(driver)
sleep(2)
date(driver)
sleep(1)
onlinePay(driver)
# Pay(driver)
sleep(1)
driver.find_element_by_xpath("//button[@ng-bind='nextPageText']").click()
sleep(1)
PayButton(driver)
sleep(5)
print YinLianem(driver)

# driver.find_element_by_xpath("").click()