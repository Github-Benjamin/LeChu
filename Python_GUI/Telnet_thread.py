# -*- coding:utf-8 -*-
from Tkinter import*
import telnetlib
import threading
import time

#Threads = []

def telent_connect():
    tn = telnetlib.Telnet(host='115.182.xxx.xxx', port=xxx, timeout=10)
    global tn
    tn.set_debuglevel(2)
    tn.write('admin' + '\n')
    tn.write('admin' + '\n')
    tn.read_until('Login success!')
    print 'Login success!'

def addItem(user,goods_id,goods_number):
    #tn.read_until('add item success.')
    tn.write('addItem %s %s %s\n'%(user,goods_id,goods_number))

def AddThread(user,goods_id,goods_number):
    Athread = threading.Thread(target=addItem,args=(user,goods_id,goods_number))
    Threads.append(Athread)

def clean_data():
    user =None
    goods_id_1=None
    goods_id_2=None
    goods_number=None
    add_number=None

telent_connect()
def telnet_lib():
    Threads = []
    global Threads
    try:
        time_one = time.time()
        user = e1.get()
        if e2.get().isdigit():
            goods_id_1 = int(e2.get())
        else:
            c['text'] = 'Data Exception'
            return 'Falied'
        if e3.get().isdigit():
            goods_id_2 = int(e3.get())+1
            if goods_id_2<goods_id_1:
                c['text'] = 'Data Exception'
                return 'Falied'
        else:
            goods_id_2=None

        goods_number = int(e4.get())
        if e5.get().isdigit():
            add_number = int(e5.get())
        else:
            add_number=1

        for i in range(add_number):
            if goods_id_2 == None:
                AddThread(user, goods_id_1, goods_number)
            else:
                for x in range(goods_id_1, goods_id_2):
                    AddThread(user, x, goods_number)

        for t in Threads:
            print t
            t.setDaemon(True)
            t.start()
        t.join()

        time_two = time.time()
        time_three = time_two-time_one
        c['text'] = 'Do Time: %s S'%round(time_three,2)
        clean_data()
        # tn.close()
    except:
        c['text'] = 'Data Exception'

root=Tk()
root.resizable(0, 0)
root.title('Benjamin H5Testing')

l = Label(root,text = 'UserName :')
l.grid(row=0,column=0,sticky=W)
e1 = Entry(root)
e1.grid(row=0,column=1,sticky=E)

l2 = Label(root,text = 'goods ID One :')
l2.grid(row=1,column=0,sticky=W)
e2 = Entry(root)
e2.grid(row=1,column=1,sticky=E)

l3 = Label(root,text = 'goods ID Two :')
l3.grid(row=2,column=0,sticky=W)
e3 = Entry(root)
e3.grid(row=2,column=1,sticky=E)

l4 = Label(root,text = 'goods_number :')
l4.grid(row=3,column=0,sticky=W)
e4 = Entry(root)
e4.grid(row=3,column=1,sticky=E)

l5 = Label(root,text = 'add_number :')
l5.grid(row=4,column=0,sticky=W)
e5 = Entry(root)
e5.grid(row=4,column=1,sticky=E)

b = Button(root,text = 'Do it',command=telnet_lib)
b.grid(row=5,column=0,sticky=E)

c = Label(root,text="")
c.grid(row=6,column=0)

root.mainloop()
