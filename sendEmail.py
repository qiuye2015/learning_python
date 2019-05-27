# coding:utf-8
# fjp

import smtplib
from email.mime.text import MIMEText
from email.header import Header

sender = 'qiuye_tju@163.com'
#receivers = '1119345739@qq.com'
receivers = ['1119345739@qq.com']
subject = 'Job'
content = "gogogogo"

message = MIMEText(content, 'plain', 'utf-8')
message['From'] = Header('qiuye_tju@163.com', 'utf-8')
message['To'] = Header('1119345739@qq.com', 'utf-8')
message['Subject'] = Header(subject, 'utf-8')
# 第三方 SMTP 服务
#mail_host = 'smtp.163.com'
mail_user = 'qiuye_tju@163.com'
mail_pass = 'yes7585151' #授权码

try:
    smtpObj = smtplib.SMTP(host='smtp.163.com',port=25)
    #smtpObj.set_debuglevel(1)
    #smtpObj.connect(mail_host,25) # host,port
    print('connect...')
    smtpObj.login(mail_user,mail_pass)
    print('login...')
    smtpObj.sendmail(sender, receivers, message.as_string())
    print('SUCCESS...')
    smtpObj.quit()
except smtplib.SMTPException as e:
    print('Error:'+format(e))

