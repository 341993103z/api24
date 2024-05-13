#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2024/4/27 14:31
# Author : smart
# @File : send_email_base.py
# @Software : PyCharm
#连接邮箱
import smtplib
#发邮件
from email.mime.text import MIMEText
#发送的对象
msg=MIMEText('邮件的内容','plain','utf-8')
#发件人
msg['From']='341993103@qq.com'
#收件人
msg['To']='341993103@qq.com'
#邮件主题
msg['Subject']='测试报告主题'
#创建一个smtp的链接
smtp=smtplib.SMTP_SSL('smtp.qq.com')
#登录发件箱
smtp.login('341993103@qq.com','nvgvhinjszswcbdc')
#发送邮件
smtp.sendmail('341993103@qq.com','341993103@qq.com',msg.as_string())
#退出 断开
smtp.quit()