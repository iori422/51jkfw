# -*- coding: utf-8 -*-
from time import sleep

from Script.WeChat.WeChatFunction.WChatObject import menu_bar, menu_menu1, order, PackageButton, onlinePay, PayButton, \
    YinLianem
from Script.WeChat.WeChatFunction.WeChatLogin import login
from Script.function.AddItems import addItems
from Script.function.Date import date
from Script.function.Information import information
from Script.function.SelectHos import SelectHos, SelectPackage

driver = login()
sleep(3)
menu_bar(driver)
sleep(1)
menu_menu1(driver)
sleep(1)
#order(driver)
driver.find_element_by_xpath("//button").click()
sleep(4)
driver.find_element_by_xpath("//div/div/label[1]").click()
# driver.find_element_by_xpath("//div/div/label[2]").click() 代他人问诊
driver.find_element_by_id("name").clear()
driver.find_element_by_id("name").send_keys(u"雷夫")
driver.find_element_by_xpath("//div[@ng-class='female']").click()
# driver.find_element_by_xpath("//div[@class='radio-female']").click() 性别女
driver.find_element_by_id("age").clear()
driver.find_element_by_id("age").send_keys("4")
driver.find_element_by_id("age").send_keys("3")
#driver.find_element_by_xpath("//div/span[text()='请选择婚姻状况']").click()
sleep(1)
#driver.find_element_by_xpath("//div/button[text()='未婚']").click()
sleep(1)
driver.find_element_by_xpath('//*[@id="view-main"]/form/fieldset/div[8]/div[1]/div').click()
sleep(1)
driver.find_element_by_xpath("//button[text()='农民']").click()
sleep(1)
driver.find_element_by_xpath("//input[@placeholder='请输入身高']").send_keys("17")
driver.find_element_by_xpath("//input[@placeholder='请输入身高']").send_keys("5")
driver.find_element_by_xpath("//input[@placeholder='请输入体重']").send_keys("60")
driver.find_element_by_xpath('//*[@id="view-main"]/form/button[2]').click()
sleep(1)
# ------------------------------------问卷-------------------------------------------------
driver.find_element_by_xpath('/html/body/div[7]/div/div/div[3]/button[1]').click()
sleep(2)
driver.find_element_by_xpath('//*[@id="question-wrapper"]/div[8]/button').click()
sleep(2)
driver.find_element_by_xpath('//*[@id="question-wrapper"]/div[5]/button[2]').click()
sleep(2)
driver.find_element_by_xpath('//*[@id="question-wrapper"]/div[7]/button[2]').click()
sleep(2)
driver.find_element_by_xpath('//*[@id="question-wrapper"]/div[18]/button[2]').click()
sleep(2)
driver.find_element_by_xpath('//*[@id="question-wrapper"]/div[13]/button[2]').click()
sleep(2)
driver.find_element_by_xpath('/html/body/div[7]/div/div/div[2]/button[2]').click()
# ------------------------------------问卷待优化--------------------------------------------
sleep(3)
driver.find_element_by_xpath('//*[@id="view-main"]/div/div[5]/div/button').click()
sleep(5)
SelectHos(driver)
sleep(3)
SelectPackage(driver)
sleep(3)
#addItems(driver)
# ------------------------------------------------------------------------------------------
sleep(1)
PackageButton(driver)
sleep(2)
information(driver)
sleep(2)
date(driver)
sleep(1)
onlinePay(driver)
# Pay(driver)
sleep(1)
driver.find_element_by_xpath("//button[@ng-bind='nextPageText']").click()
sleep(2)
PayButton(driver)
sleep(5)
c= YinLianem(driver)
print c