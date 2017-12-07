# -*- coding: utf-8 -*-
import random
from  selenium import webdriver
def selectDay(driver):
   days = driver.find_elements_by_xpath("//td[@class='new day']")
   day =random.choice(days)
   day.click()
   print days,day

   # a= random.choice(len(days))
   # print days[a]
   # days[a].click()