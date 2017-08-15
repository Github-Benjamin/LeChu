import requests
import time

def additem(user,id,number):
    time.sleep(0.02)
    html = requests.get(url='http://115.182.xx.xx:xxxx/manage/addItem?accountName=%s&itemTemplateId=%s&count=%s'%(user,id,number)).text
    print html

user = 'test8156'
number = '1'

for i in range(504001,504026):
    additem(user,i,number)

# html = requests.get(url='http://115.182.xx.xx:xxxx/manage/addItem?accountName=test8155&itemTemplateId=256&count=100').text
# print html
