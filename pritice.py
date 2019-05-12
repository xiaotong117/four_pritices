#!/usr/bin/python
# -*- coding: UTF-8 -*- 

import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

# 发邮件
my_sender = 'zhangt@shinemo.com'  # 发件人邮箱账号，为了后面易于维护，所以写成了变量
my_user = 'zhangt@shinemo.com'  # 收件人邮箱账号，为了后面易于维护，所以写成了变量
try:
    msg = MIMEText('填写邮件内容', 'plain', 'utf-8')
    msg['From'] = formataddr(["系统通知", my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
    msg['To'] = formataddr(["收件人邮箱账号人邮箱昵称", my_user])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
    msg['Subject'] = "对账出错！"  # 邮件的主题，也可以说是标题
    server = smtplib.SMTP()  # 发件人邮箱中的SMTP服务器，端口是25
    server.connect("smtp.exmail.qq.com", 465)
    server.login(my_sender, "12345qWE")  # 括号中对应的是发件人邮箱账号、邮箱密码
    server.sendmail(my_sender, my_user, msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
    server.quit()  # 这句是关闭连接的意思

except:
    print('123')# 如果try中的语句没有执行，则会执行下面的ret=False