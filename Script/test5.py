# -*- coding: utf-8 -*-
import hashlib
from time import sleep

from  selenium import webdriver

import string, random
import datetime

now_time = datetime.datetime.now()

print now_time

# look_set = string.ascii_letters + string.digits
# md5_len = 32
# tmp_md5_ls = []
# for k in range(500):
#     for i in range(md5_len):
#         tmp_md5_ls.append(random.choice(look_set))
#     print ''.join(tmp_md5_ls)
#     tmp_md5_ls = []


myprofile=webdriver.FirefoxProfile(r"C:\Users\Administrator\AppData\Roaming\Mozilla\Firefox\Profiles\z13uqgmd.Test")
driver =webdriver.Firefox()
driver.set_window_size(310,710)
driver.get("http://demo.tijianzhuanjia.com/wx/index.html?sid=00-0#/login?state={%22name%22:%22userCenter%22,%22params%22:{},%22options%22:{}}")
sleep(3)
driver.find_element_by_xpath("//*[@id='username']").send_keys("18011111128")
driver.find_element_by_xpath("//*[@id='password']").send_keys("111111")
d = driver.find_element_by_xpath('#viewport > form > button')


