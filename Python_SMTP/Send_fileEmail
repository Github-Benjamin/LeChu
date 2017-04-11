# coding:utf8
from smtplib import SMTP_SSL
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

mail_info = {
    "hostname": "smtp.qq.com",

    "from": "benjamin_v@qq.com",
    "to": "350105xxx@qq.com",

    "mail_subject": "Python SMTP Send File Testig.....",
    "mail_text": '<html><body><h1>Hello</h1>' +
                 '<p>Send file Testing</p>' +
                 '<p>send by <a href="http://www.python.org">http://www.python.org</a>...</p>' +
                 '</body></html>',
}

smtp = SMTP_SSL(mail_info["hostname"])


def login_QQEmail():
    # 这里使用SMTP_SSL就是默认使用465端口
    smtp.set_debuglevel(1)
    smtp.ehlo(mail_info["hostname"])
    smtp.login("benjamin_v@qq.com", "mqrgvfzavxxxxxx")

file_path = 'C:\\Users\\xxxxx\\Desktop\\python_testing.txt'

def msg_info():
    msg = MIMEMultipart()
    
    #msg = MIMEText(mail_info["mail_text"], "html", "utf-8")
    msg["Subject"] = Header(mail_info["mail_subject"], "utf-8")
    msg["from"] = mail_info["from"]
    msg["to"] = mail_info["to"]
    msg.attach(MIMEText(mail_info["mail_text"], "html", "utf-8"))


    att1 = MIMEText(open(file_path,'rb').read(),'base64','utf-8')
    att1["Content-Type"] = 'application/octet-stream'
    # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
    att1["Content-Disposition"] = 'attachment; filename="python_testing.txt"'
    #print att1.as_string()
    msg.attach(att1)

    smtp.sendmail(mail_info["from"], mail_info["to"], msg.as_string())
    #print  msg.as_string()

if __name__ == '__main__':
    login_QQEmail()
    msg_info()
    smtp.quit()
