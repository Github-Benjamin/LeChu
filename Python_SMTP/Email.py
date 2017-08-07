# condig:utf-8
import smtplib
import string
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

HOST = 'smtp.qq.com'
SUBJECT = 'Test email form Python'
TO = '350105xxx@qq.com'
FROM = 'Benjamin_v@qq.com'
text = 'Python rules them all!'

BODY = string.join((
    "From:%s"%FROM,
    "To:%s"%TO,
    "Subject:%s"%SUBJECT,
    "",
    text),"\r\n")

def Login_Email():
    global server
    server = smtplib.SMTP()
    server.connect(HOST,'25')
    server.starttls()
    server.login("Benjamin_v@qq.com","tavplxghnvixxxx")

def Send_Email(BODY):
    server.sendmail(FROM,TO,BODY)
    server.quit()

Login_Email()
Send_Email()

