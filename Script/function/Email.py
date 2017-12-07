#!/usr/bin/env python
#coding: utf-8
      
'''''
    FuncName: smtplib_email.py 
    Desc: 使用smtplib发送邮件 
    Date: 2016-04-11 14:00 
    Author: johnny 
    '''
      
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.utils import COMMASPACE,formatdate
from email import encoders
      
def send_email_text(sender,receiver,host,subject,text,filename):

    assert type(receiver) == list

    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = COMMASPACE.join(receiver)
    msg['Subject'] = subject
    msg['Date'] = formatdate(localtime=True)
    msg.attach(MIMEText(text))                 #邮件正文内容

    for file in filename:                      #邮件附件
        att = MIMEBase('application', 'octet-stream')
        att.set_payload(open(file, 'rb').read())
        encoders.encode_base64(att)
        if file.endswith('.html'):             # 若不加限定，jpg、html等格式附件是bin格式的
            att.add_header('Content-Disposition', 'attachment; filename="今日测试结果.html"')          # 强制命名，名称未成功格式化，如果可以解决请联系我
        elif file.endswith('.jpg') or file.endswith('.png') :
            att.add_header('Content-Disposition', 'attachment; filename="pic.jpg"')
        else:
            att.add_header('Content-Disposition', 'attachment; filename="%s"' % file)
        msg.attach(att)

    smtp = smtplib.SMTP(host)
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    smtp.login(username,password)
    smtp.sendmail(sender,receiver, msg.as_string())
    smtp.close()

if __name__=="__main__":
    sender = 'qqq@163.com'
    receiver = ['www@qq.com']
    subject = "测试"
    text = "johnny'lab test"
    filename = [u'测试报告.html','123.txt',u'获取的信息.jpg']
    host = 'smtp.163.com'
    username =  'qqq@163.com'
    password =  'qqq'
    send_email_text(sender,receiver,host,subject,text,filename)