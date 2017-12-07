# -*- coding: utf-8 -*-
from time import sleep
import urllib2

from  selenium import webdriver
def pay(driver):
  for g in range(0,3):
    b=driver.find_elements_by_xpath("//ins")
    b[g].click()
    sleep(1)
    driver.find_element_by_id('pay').click()
    p = driver.window_handles
    driver.switch_to_window(p[1])
    c = driver.current_url
    print c
    req = urllib2.Request(c)
    try:
       urllib2.urlopen(req)
    except urllib2.HTTPError,e:
      print e.code
      print e.reason
    driver.close()
    driver.switch_to_window(p[0])
    driver.find_element_by_xpath("//a[@class='text-info']").click()
    sleep(1)
  e = driver.window_handles
  driver.switch_to_window(e[0])


