# -*- coding: utf-8 -*-
from time import sleep

from selenium import webdriver
import  MySQLdb

#from Script.baogao_xsl import code, user_name
from Script.Import_Report import Import_report
from Script.sql import sql_conn
from Script.test1 import sql_username





name =sql_username()# 体检报告名字
sql  = sql_conn()
cur = sql.cursor()
aa = cur.execute("select * from `key` where card_state = 0 order by card_state DESC limit 0,1")
pp = cur.fetchall()
bb = cur.execute("UPDATE `key` SET card_state = 1 "
                 "WHERE card_state = 0 order by card_state DESC limit 1")

sql.commit()
cord_psw= pp[0][2]
print cord_psw

myprofile=webdriver.FirefoxProfile(r"C:\Users\Administrator\AppData\Roaming\Mozilla\Firefox\Profiles\z13uqgmd.Test")
driver =webdriver.Firefox()
driver.set_window_size(310,710)
driver.get("http://show.tijianzhuanjia.com/wx/index.html?sid=00-0#/login?state={%22name%22:%22userCenter%22,%22params%22:{},%22options%22:{}}")
sleep(3)
driver.find_element_by_xpath("//*[@id='username']").send_keys("18011111132")
driver.find_element_by_xpath("//*[@id='password']").send_keys("111111")
driver.find_element_by_xpath('//*[@id="viewport"]/form/button').click()
sleep(3)
driver.find_element_by_xpath("//*[@id=\"foot_bar\"]/li[1]/span[1]").click()
sleep(1)
driver.find_element_by_xpath("//*[@id=\"view-main\"]/div[3]/div/ul/li[3]/a/span[1]").click()

# driver.find_element_by_xpath('//*[@id="view-main"]/div[2]/div[1]/div/ul/li[2]/div').click()
sleep(5)
# try:
#     driver.find_element_by_xpath("//*[@id='index']/div[1]").click()
#     sleep(2)
# except:
#     driver.find_element_by_xpath('//*[@id="view-main"]/div[2]').click()
#     sleep(2)
driver.find_element_by_xpath('//*[@id="view-main"]/div/button[2]').click()
sleep(2)
driver.find_element_by_xpath('//*[@id="view-main"]/div/div/div[1]/input').send_keys(cord_psw)
driver.find_element_by_xpath('//*[@id="view-main"]/div/div/div[1]/button').click()
sleep(3)
driver.find_element_by_xpath('//*[@id="view-main"]/form[2]/div[8]/div[1]/input').clear()
driver.find_element_by_xpath('//*[@id="view-main"]/form[2]/div[8]/div[1]/input').send_keys("18")
driver.find_element_by_xpath('//*[@id="view-main"]/form[2]/div[8]/div[1]/input').send_keys("1")
driver.find_element_by_xpath('//*[@id="view-main"]/form[2]/div[2]/div/input').clear()
driver.find_element_by_xpath('//*[@id="view-main"]/form[2]/div[2]/div/input').send_keys(name)
driver.find_element_by_xpath('//*[@id="view-main"]/form[2]/button').click()
sleep(2)
driver.find_element_by_xpath('/html/body/div[7]/div/div/div[2]/button').click()
sleep(2)
driver.find_element_by_xpath('/html/body/div[7]/div/div/div[2]/button[1]').click()
sleep(5)
driver.find_element_by_xpath('/html/body/div[7]/div/div/div[2]/button[2]').click()
sleep(2)
#----------------------------------生活问卷----------------------------------------------
driver.find_element_by_id('sport0001opt001').click()
driver.find_element_by_id('sport0002opt002').click()
driver.find_element_by_id('sport0009opt022').click()
driver.find_element_by_id('sport0004opt001').click()
driver.find_element_by_id('sport0005opt001').click()
driver.find_element_by_id('sport0006opt001').click()
driver.find_element_by_id('sport0007opt004').click()
driver.find_element_by_id('sport0008opt004').click()
#----------------------------------生活问卷----------------------------------------------
sleep(2)

driver.find_element_by_xpath("//*[@id='question-wrapper']/div[11]/button").click()
sleep(2)
driver.find_element_by_xpath("/html/body/div[7]/div/div/div[2]/button[2]").click()
sleep(5)
driver.find_element_by_xpath("//*[@id='mzf0043-text']").clear()
driver.find_element_by_xpath("//*[@id='mzf0043-text']").send_keys(180)
driver.find_element_by_xpath("//*[@id='mzf0044-text']").clear()
driver.find_element_by_xpath("//*[@id='mzf0044-text']").send_keys(80)

# driver.find_element_by_xpath("/html/body/div[7]/div/div/div[2]/button[2]").clear()
# driver.find_element_by_xpath("/html/body/div[7]/div/div/div[2]/button[2]").send_keys('80')
sleep(2)
driver.find_element_by_xpath("//*[@id='question-wrapper']/div[15]/button").click()
sleep(2)
driver.find_element_by_xpath("//*[@id='question-wrapper']/div[7]/button[2]").click()
sleep(2)
driver.find_element_by_xpath("//*[@id='question-wrapper']/div[11]/button[2]").click()
sleep(2)
driver.find_element_by_xpath("/html/body/div[7]/div/div/div[2]/button[2]").click()
sleep(2)
driver.find_element_by_xpath("//html/body/div[7]/div/div/div[2]/button").click()

















# driver.find_element_by_xpath('//*[@id="view-main"]/form[2]/div[9]/div[1]/input').clear()
# driver.find_element_by_xpath('//*[@id="view-main"]/form[2]/div[9]/div[1]/input').send_keys("60")
# driver.find_element_by_xpath('//*[@id="view-main"]/form[2]/button').click()
# sleep(2)
# driver.find_element_by_xpath('/html/body/div[6]/div/div/div[2]/button').click()
# sleep(3)
# try:
#     driver.find_element_by_xpath('/html/body/div[6]/div/div/div[2]/button[1]').click()
# except:
#     driver.find_element_by_xpath('/html/body/div[6]/div/div/div[2]/button[2]').click()
# sleep(3)
# driver.find_element_by_xpath('/html/body/div[6]/div/div/div[2]/button[2]').click()
#
# # driver.find_element_by_xpath('//*[@id="gth02gt00000600_gt00000601"]').click()
# driver.find_element_by_xpath('//*[@id="gth02gt00000600_gt00000602"]').click()

#
# code
# user_name
