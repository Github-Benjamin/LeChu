from Tkinter import*
import telnetlib
import time

Host = '115.182.xx.xx'
Port = 'xxxx'
username = 'admin'
password = 'admin'

def telnet():
    tn = telnetlib.Telnet(Host, port=xxxxx, timeout=10)
    global tn
    tn.set_debuglevel(2)

def telent_connect(user):
    telnet()
    # input username
    tn.read_until('Please input user name:')
    tn.write(username + '\n')

    # input password
    tn.read_until('Please input password:')
    tn.write(password + '\n')
    tn.read_until('Login success!')
    #print 'Login success!'
    tn.write('addItem %s 200 1\n'%(user))

def AddItem(user,goods_id,goods_nubmer):
    tn.read_until('add item success.')
    tn.write('addItem %s %s %s\n'%(user,goods_id,goods_nubmer))

def MainAddItem(goods_id_one,goods_id_two,add_goods_number,user,goods_nubmer):
    if goods_id_two ==None :
        for i in range(add_goods_number):
            AddItem(user,goods_id_one,goods_nubmer)
        #tn.close()
        #print 'colse telnet'
    else:
        for i in range(goods_id_one,goods_id_two):
            AddItem(user,i,goods_nubmer)
        #tn.close()
    #tn.close()

def clean_data():
    user =None
    goods_id_one=None
    goods_id_two=None
    goods_nubmer=None
    add_goods_number=None

def telnet_lib():
    try:
        time_one = time.time()
        user = e1.get()
        goods_id_one = int(e2.get())
        if e3.get().isdigit():
            goods_id_two = int(e3.get())+1
        else:
            goods_id_two=None
        goods_nubmer = int(e4.get())
        if e5.get().isdigit():
            add_goods_number = int(e5.get())
        else:
            add_goods_number=1
        #print user,goods_id_one,goods_id_two,goods_nubmer,add_goods_number
        telent_connect(user)
        MainAddItem(goods_id_one,goods_id_two,add_goods_number,user,goods_nubmer)
        time_two = time.time()
        time_three = time_two-time_one
        c['text'] = 'Do Time: %s S'%round(time_three,2)
        clean_data()
        tn.close()
    except:
        c['text'] = 'input data exception'

root=Tk()
root.resizable(0, 0)
root.title('Benjamin H5Testing')
#root.wm_iconbitmap('Benjamin.ico')

l = Label(root,text = 'UserName:')
l.grid(row=0,column=0,sticky=W)
e1 = Entry(root)
e1.grid(row=0,column=1,sticky=E)

l2 = Label(root,text = 'goods ID One:')
l2.grid(row=1,column=0,sticky=W)
e2 = Entry(root)
e2.grid(row=1,column=1,sticky=E)

l3 = Label(root,text = 'goods ID two:')
l3.grid(row=2,column=0,sticky=W)
e3 = Entry(root)
e3.grid(row=2,column=1,sticky=E)

l4 = Label(root,text = 'goods_nubmer:')
l4.grid(row=3,column=0,sticky=W)
e4 = Entry(root)
e4.grid(row=3,column=1,sticky=E)

l5 = Label(root,text = 'add_goods_number:')
l5.grid(row=4,column=0,sticky=W)
e5 = Entry(root)
e5.grid(row=4,column=1,sticky=E)

b = Button(root,text = 'Do it',command=telnet_lib)
b.grid(row=5,column=0,sticky=E)

c = Label(root,text="")
c.grid(row=6,column=0)

root.mainloop()
