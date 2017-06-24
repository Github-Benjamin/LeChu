import paramiko
import ftplib
import os
import time
import socket
import random
import hashlib

print '######################\nSSH , FTP  Loading...'
socket.setdefaulttimeout(3)
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ftp = ftplib.FTP()

def input_key():
    global number
    number = '%s'%random.randint(100000, 999999)
    key_number = number+'Benjamin'+number[5]+number[4]
    return key_number

def keytoken(key_number):
    m2 = hashlib.md5()
    m2.update(key_number)
    key =  m2.hexdigest()
    return key

def connect():
    try:
        ssh.connect(hostname='192.168.1.1', port=22, username='root', password='Anonymous',allow_agent=False,look_for_keys=False)
        ftp.connect('192.168.1.1',21)
        ftp.login('root','Anonymous')
        ftp.cwd("/root")
        print '######################\nSSH , FTP Load Sucess!\n######################'
        return True
    except:
        print '######################\nSSH , FTP Load Failed!\n######################'
        time.sleep(60)
        return False

def domain():
        username = raw_input('Please input username: ')
        password = raw_input('Please input password: ')
        host_ip = raw_input('Please input host_ip: ')
        mac = raw_input('Please input mac: ')

        file = open('drcomone','w+')
        configdata = '''# -*- coding:utf-8 -*-

f1 = file("/usr/bin/drcom")
f2 = file("/etc/drcom.conf",'w+')

data="""server = '10.255.255.250'
username = '%s'
password = '%s'
CONTROLCHECKSTATUS = '\\\\x20'
ADAPTERNUM = '\\\\x04'
host_ip = '%s'
IPDOG = '\\\\x01'
host_name = 'Kali'
PRIMARY_DNS = '10.255.0.193'
dhcp_server = '10.255.0.197'
AUTH_VERSION = '\\\\x28\\\\x00'
mac = 0x%s
host_os = 'Kali'
KEEP_ALIVE_VERSION = '\\\\xdc\\\\x02'"""

listf1 = f1.readlines()
del listf1[8:22]
listf1.insert(8,'\\n')
listf1.insert(8,data)
f1.close()

f1 = file("/usr/bin/drcom",'w+')
for i in listf1:
    f1.write(i)
f1.closed

f2.write(data)
f2.close()'''%(username,password,host_ip,mac)

        file.write(configdata)
        file.close()

        stdin, stdout, stderr = ssh.exec_command('rm -f drcomone')
        time.sleep(1)

        localfile = 'drcomone'
        f = open(localfile,'rb')
        ftp.storbinary('STOR %s' % os.path.basename(localfile), f)

        time.sleep(1)
        stdin, stdout, stderr = ssh.exec_command('python drcomone')
        time.sleep(1)
        stdin, stdout, stderr = ssh.exec_command('rm -f drcomone')
        stdin, stdout, stderr = ssh.exec_command('reboot')

        f.close()
        ssh.close()
        print '\n######################\nThe End,Now Check your router!\n######################'
        time.sleep(60)

key = keytoken(input_key())
error = 0
if connect():
    while error<=2:
        input_key = raw_input('CipherText:%s, Please input Key: '%number)
        if  input_key == key:
            print '\nLogin sucess!\n'
            domain()
            break
        else:
            error += 1
            print 'Key error %s'%error
            if error == 3:
                print '\nThe end,Error more than 3 times!'
                time.sleep(60)
            continue
else:
    pass
