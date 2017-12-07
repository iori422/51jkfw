# -*- coding: utf-8 -*-
from  selenium import webdriver
import urllib2,urllib
def template01():
 url = 'https://demo.tijianzhuanjia.com/sms-service/sms-service/sms'
 phoneno = 18075193137
 tim = "sendTime"
 timto = "2016-04-28 15:10:00"
 data = {'telephone':phoneno,
         'signatureCode':'身份验证',
         'product':'体检砖家',
         'code':'template01',
         'expiration':'ssss',
         tim:timto
         }
 data = urllib.urlencode(data)
 url2 = urllib2.Request(url,data)
 response = urllib2.urlopen(url2)
 apicontent = response.read()
 print  apicontent

def template02():
 url = 'https://demo.tijianzhuanjia.com/sms-service/sms-service/sms'
 phoneno = 18075193137
 data = {'telephone':phoneno,
         'signatureCode':'身份验证',
         'product':'体检砖家',
         'code':'template02',
         'expiration':'ssss',
         }
 data = urllib.urlencode(data)
 url2 = urllib2.Request(url,data)
 response = urllib2.urlopen(url2)
 apicontent = response.read()
 print  apicontent


def template03():
 url = 'https://demo.tijianzhuanjia.com/sms-service/sms-service/sms'
 phoneno = 18075193137
 data = {'telephone':phoneno,
         'signatureCode':'身份验证',
         'product':'体检砖家',
         'code':'template03',
         'reportNo':'TEST01',
         'reportType':'健康管理专家'}
 data = urllib.urlencode(data)
 url2 = urllib2.Request(url,data)
 response = urllib2.urlopen(url2)
 apicontent = response.read()
 print  apicontent



def template04():
 url = 'https://demo.tijianzhuanjia.com/sms-service/sms-service/sms'
 phoneno = 18075193137
 data = {'telephone':phoneno,
         'signatureCode':'身份验证',
         'product':'体检砖家',
         'code':'template04',
         'expiration':'ssss'}
 data = urllib.urlencode(data)
 url2 = urllib2.Request(url,data)
 response = urllib2.urlopen(url2)
 apicontent = response.read()
 print  apicontent


def template05():
 url = 'https://demo.tijianzhuanjia.com/sms-service/sms-service/sms'
 phoneno = 18075193137
 data = {'telephone':phoneno,
         'signatureCode':'身份验证',
         'product':'体检砖家',
         'code':'template05',
         'expiration':'ssss',}
 data = urllib.urlencode(data)
 url2 = urllib2.Request(url,data)
 response = urllib2.urlopen(url2)
 apicontent = response.read()
 print  apicontent


def template06():
 url = 'https://demo.tijianzhuanjia.com/sms-service/sms-service/sms'
 phoneno = 18075193137
 data = {'telephone':phoneno,
         'signatureCode':'身份验证',
         'product':'体检砖家',
         'code':'template06',
         'reportNo':'000001'}
 data = urllib.urlencode(data)
 url2 = urllib2.Request(url,data)
 response = urllib2.urlopen(url2)
 apicontent = response.read()
 print  apicontent

def template07():
 url = 'https://demo.tijianzhuanjia.com/sms-service/sms-service/sms'
 phoneno = 18075193137
 data = {'telephone':phoneno,
         'signatureCode':'身份验证',
         'product':'体检砖家',
         'code':'template07',
         'reportNo':'000001',
         'ADate':'2016-4-29',
         'CCenter':'湘雅附三'}
 data = urllib.urlencode(data)
 url2 = urllib2.Request(url,data)
 response = urllib2.urlopen(url2)
 apicontent = response.read()
 print  apicontent


def template08():
 url = 'https://demo.tijianzhuanjia.com/sms-service/sms-service/sms'
 phoneno = 18075193137
 data = {'telephone':phoneno,
         'signatureCode':'身份验证',
         'product':'体检砖家','code':'template08',
         'name':'罗拉',
         'reportNo':'000001',
         'ADate':'2016-4-29',
         'CCenter':'湘雅附三'}
 data = urllib.urlencode(data)
 url2 = urllib2.Request(url,data)
 response = urllib2.urlopen(url2)
 apicontent = response.read()
 print  apicontent

def template09():
 url = 'https://demo.tijianzhuanjia.com/sms-service/sms-service/sms'
 phoneno = 18075193137
 data = {'telephone':phoneno,
         'signatureCode':'身份验证',
         'product':'体检砖家','code':'template09',
         'name':'罗拉',
         'reportNo':'000001',
         'period':'2016-8-04',
         'CCenter':'湘雅附三',
         'Tips':'建议早上空腹体检'}
 data = urllib.urlencode(data)
 url2 = urllib2.Request(url,data)
 response = urllib2.urlopen(url2)
 apicontent = response.read()
 print  apicontent


def template10():
 url = 'https://demo.tijianzhuanjia.com/sms-service/sms-service/sms'
 phoneno = 18075193137
 data = {'telephone':phoneno,
         'signatureCode':'身份验证',
         'product':'体检砖家','code':'template10',
         'name':'罗拉',
         'reportNo':'000001',
         'period':'2016-8-04',
         'CCenter':'湘雅附三'
         }
 data = urllib.urlencode(data)
 url2 = urllib2.Request(url,data)
 response = urllib2.urlopen(url2)
 apicontent = response.read()
 print  apicontent


def template11():
 url = 'https://demo.tijianzhuanjia.com/sms-service/sms-service/sms'
 phoneno = 18075193137
 data = {'telephone':phoneno,
         'signatureCode':'身份验证',
         'product':'体检砖家','code':'template11',
         'money':'108.00',
         'period':'2016-8-04',
         }
 data = urllib.urlencode(data)
 url2 = urllib2.Request(url,data)
 response = urllib2.urlopen(url2)
 apicontent = response.read()
 print  apicontent


def template12():
 url = 'https://demo.tijianzhuanjia.com/sms-service/sms-service/sms'
 phoneno = 18075193137
 data = {'telephone':phoneno,
         'signatureCode':'身份验证',
         'product':'体检砖家','code':'template12',
         'CCenter':'湘雅附三',
         }
 data = urllib.urlencode(data)
 url2 = urllib2.Request(url,data)
 response = urllib2.urlopen(url2)
 apicontent = response.read()
 print  apicontent


def template13():
 url = 'https://demo.tijianzhuanjia.com/sms-service/sms-service/sms'
 phoneno = 18075193137
 data = {'telephone':phoneno,
         'signatureCode':'身份验证',
         'product':'体检砖家',
         'code':'template13',
         'company':'中建集团',
         }
 data = urllib.urlencode(data)
 url2 = urllib2.Request(url,data)
 response = urllib2.urlopen(url2)
 apicontent = response.read()
 print  apicontent


def template301():
 url = 'https://demo.tijianzhuanjia.com/sms-service/sms-service/sms'
 phoneno = 18075193137
 data = {'telephone':phoneno,
         'signatureCode':'身份验证',
         'product':'体检砖家','code':'301Examinationnotify',
         'name':'潇潇',
         'adate':'2016-4-28',
         'cdate':'2016-5-30'
         }
 data = urllib.urlencode(data)
 url2 = urllib2.Request(url,data)
 response = urllib2.urlopen(url2)
 apicontent = response.read()
 print  apicontent

def templatevoice01():
 url = 'https://demo.tijianzhuanjia.com/sms-service/sys/tts/singlecall'
 phoneno = 18075193137
 data = {'telephone':phoneno,
         'calledShowNum':'4008817190',
         'code':'template01',
         'expiration':'30'}
 data = urllib.urlencode(data)
 url2 = urllib2.Request(url,data)
 response = urllib2.urlopen(url2)
 apicontent = response.read()
 print  apicontent

def templatevoice02():
 url = 'https://demo.tijianzhuanjia.com/sms-service/sys/tts/singlecall'
 phoneno = 18075193137
 data = {'telephone':phoneno,
         'calledShowNum':'4008817190',
         'code':'template02',
         'expiration':'30'}
 data = urllib.urlencode(data)
 url2 = urllib2.Request(url,data)
 response = urllib2.urlopen(url2)
 apicontent = response.read()
 print  apicontent

def templatevoice04():
 url = 'https://demo.tijianzhuanjia.com/sms-service/sys/tts/singlecall'
 phoneno = 18075193137
 data = {'telephone':phoneno,
         'calledShowNum':'4008817190',
         'code':'template04',
         'expiration':'30秒'}
 data = urllib.urlencode(data)
 url2 = urllib2.Request(url,data)
 response = urllib2.urlopen(url2)
 apicontent = response.read()
 print  apicontent

templatevoice04()

