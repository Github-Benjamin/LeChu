#coding:utf8
from smtplib import SMTP_SSL
from email.header import Header
from email.mime.text import MIMEText

mail_info = {
    "hostname": "smtp.qq.com",

    "username": "benjamin_v@qq.com",
    "password": "mqrgvfzavzxxxxxxx",

    "from": "benjamin_v@qq.com",
    "to": "350105xxx@qq.com",

    "mail_subject": "Testing Python SMTP Send Email！",
    "mail_text": "<html><body><h1>Hello</h1>' +
    '<p>send by <a href="http://www.python.org">http://www.python.org</a>...</p>' +
    '</body></html>",
}

smtp = SMTP_SSL(mail_info["hostname"])

def login_QQEmail():
    #这里使用SMTP_SSL就是默认使用465端口
    smtp.set_debuglevel(1)
    smtp.ehlo(mail_info["hostname"])
    smtp.login(mail_info["username"], mail_info["password"])

def msg_info():
    msg = MIMEText(mail_info["mail_text"], "html","utf-8")
    msg["Subject"] = Header(mail_info["mail_subject"],"utf-8")
    msg["from"] = mail_info["from"]
    msg["to"] = mail_info["to"]
    smtp.sendmail(mail_info["from"], mail_info["to"], msg.as_string())
    #print  msg.as_string()

if __name__ == '__main__':
    login_QQEmail()
    msg_info()
    smtp.quit()
