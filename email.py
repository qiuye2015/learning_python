# coding:utf-8
# fjp

import smtplib
from email.mime.text import MIMEText
from email.header import Header

sender = "from@qq.com"
receivers = ['1119345739@qq.com']
subject = 'python 邮件主题'

message = MIMEText('python 邮件发送测试', 'plain', 'utf-8')
message['From'] = Header("发送者", 'utf-8')
message['To'] = Header('接收者', 'utf-8')
message['Subject'] = Header(subject, 'utf-8')

try:
    smtpObj = smtplib.SMTP('localhost')
    smtpObj.sendemail(sender.receivers, message.as_string())
    print('邮件发送成功')
except smtplib.SMTPException:
    print('Error:无法发送邮件')
