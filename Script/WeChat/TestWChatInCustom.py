# -*- coding: utf-8 -*-
from time import sleep
import document
from  selenium import webdriver

from Script.WeChat.WeChatFunction.WChatObject import menu_bar, menu_menu1
from Script.function.Code import ident_generator
from Script.WeChat.WeChatFunction.WeChatLogin import login
driver = login()
sleep(3)
# --------------------------wechat登录页面-------------------------------
menu_bar(driver)
sleep(1)
menu_menu1(driver)
sleep(2)
driver.find_element_by_xpath("/html/body/section/ul/li[2]").click()
sleep(10)
driver.find_element_by_xpath("//ul[@class=\"list-group\"]/li[2]").click()
driver.find_element_by_xpath("//div/img[@ng-src]").click()
sleep(3)
driver.find_element_by_id("name").clear()
driver.find_element_by_id("name").send_keys(u"溜溜溜溜")
# driver.find_element_by_id("boCellPhoneNo").clear()
# driver.find_element_by_id("boCellPhoneNo").send_keys("18011111131")
driver.find_element_by_id("identityCardNo").clear()
sleep(1)
# ---------------------------------------个人信息--------------------------------------------
driver.find_element_by_id("identityCardNo").clear()
code = ident_generator()
print code
for j in range(len(code)):
    print code[j]
    driver.find_element_by_xpath("//div[3]/div[@class='col-xs-9']/input").send_keys(code[j])
driver.find_element_by_xpath("//input[@min]").clear()
driver.find_element_by_xpath("//input[@min]").send_keys("25")
driver.find_element_by_xpath("//label[2]/div").click()
# driver.find_element_by_xpath("//label[1]/div").click()
driver.find_element_by_xpath("//button").click()
# --------------------------------------个人信息--------------------------------------------
sleep(3)
driver.find_element_by_xpath("//span[text()='添加']").click()
sleep(2)
driver.find_element_by_id("keyword").send_keys(u"糖化血红蛋白")
driver.find_element_by_xpath("//div[text()='搜索']").click()
sleep(2)
driver.execute_script("var a=document.getElementsByClassName(\"panel-heading\")[2];a.click();")
# 调用JS点击class=panel-heading
driver.execute_script("var a=document.getElementsByClassName(\"icheckbox_flat-green\")[11];a.click();")
sleep(2)
driver.find_element_by_xpath("//button").click()
sleep(2)
TJXM= driver.find_element_by_xpath("//span[@ng-bind='recommendProjectPrice | number:2']").text
ZXXM= driver.find_element_by_xpath("//span[@ng-bind='customProjectsPrice | number:2']").text
GLXM= driver.find_element_by_xpath("//span[@ng-bind='materialProjectPrice | number:2']").text
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
date(driver)
# ----------------------------------------------选择日期组件------------------------------------------
sleep(2)
try:
    driver.find_element_by_xpath("//label[@class='pay-check pay-check-block ']").click()# 在线支付
    driver.find_element_by_xpath("//button[text()='提交订单']").click()
    driver.find_element_by_id("pay").click()
except:
    driver.find_element_by_xpath("//label[@class='pay-check pay-check-block m-t-10 ']").click()# 医院支付
    driver.find_element_by_xpath("//button[text()='提交订单']").click()



