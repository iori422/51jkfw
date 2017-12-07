# -*- coding: utf-8 -*-
from time import sleep
from  selenium import webdriver
import random


def nav_menu(driver):#首页“体检预约”
  driver.find_element_by_xpath("//a[text()='体检预约']").click()
  return

def ind_start(driver):#检前问诊开始按钮
  driver.find_element_by_xpath("//a[@class='ind-start']").click()
  return

def inputmessage(driver):#填写个人资料
  driver.find_element_by_id("name").clear()
  driver.find_element_by_id("name").send_keys(u"牛能")
  driver.find_element_by_xpath("//label/div[@class='iradio_flat-green']").click()
  driver.find_element_by_xpath("//input[@name='age']").clear()
  driver.find_element_by_xpath("//input[@name='age']").send_keys('25')
  sleep(2)
  m=driver.find_element_by_xpath("//div/select[@name='marriageCode']")
  m.find_element_by_xpath("//option[@value='married']").click()
  m1="find_element_by_xpath(\"//option[@value='married']\").click()"
  m2="find_element_by_xpath(\"//option[@value='unmarried']\").click()"
  # 选择婚姻状况
  # no = str(random.randint(1, 58))
  # print no
  # a="\"//option[@value="+no+"]\""
  # driver.find_element_by_xpath(a).click()
  nation=driver.find_element_by_xpath("//select[@name='folkCode']")
  nation.find_element_by_xpath("//option[@value='7']").click()
  # 选择民族
  job=driver.find_element_by_xpath("//select[@name='professionCode']")
  job.find_element_by_xpath("//option[text()='工人']").click()
  # 选择职业
  driver.find_element_by_xpath("//input[@name='height']").send_keys('172')
  driver.find_element_by_xpath("//input[@name='weight']").send_keys('60')
  driver.find_element_by_xpath("//button[@type='submit']").click()
  #个人资料

  return





