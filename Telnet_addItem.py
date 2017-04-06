# -*- coding: utf-8 -*-
import telnetlib
import time

Host = '115.182.xx.xx'
Port = 'xxxxxx'
username = 'admin'
password = 'admin'

tn = telnetlib.Telnet(Host, port=38080, timeout=10)
tn.set_debuglevel(2)

def telent_connect(user):
    # input username
    tn.read_until('Please input user name:')
    tn.write(username + '\n')

    # input password
    tn.read_until('Please input password:')
    tn.write(password + '\n')
    tn.read_until('Login success!')
    print 'Login success!'
    tn.write('addItem %s 200 1\n'%(user))

def addItem(user,goods_id,goods_nubmer):
    tn.read_until('add item success.')
    tn.write('addItem %s %s %s\n'%(user,goods_id,goods_nubmer))

def mainaddItem(goods_id_one,goods_id_two,add_goods_number):
    if goods_id_two ==None :
        for i in range(add_goods_number):
            addItem(user,goods_id_one,goods_nubmer)
    else:
        for i in range(goods_id_one,goods_id_two):
            addItem(user,i,goods_nubmer)

if __name__=='__main__':

    time_one = time.time()

    user = '{userame}'
    telent_connect(user)

    goods_id_one = 31
    goods_id_two = None
    goods_nubmer = 30

    add_goods_number = 3

    mainaddItem(goods_id_one,goods_id_two,add_goods_number)
    tn.close()

    time_two = time.time()
    time_three = time_two-time_one
    print '\nTiem: %s S'%round(time_three,2)
