import pickle
import socket
from random import *
from os import listdir
from os.path import isfile, join
from re import *

HOST = socket.gethostname()
PORT = 12345

s = socket.socket()
s.bind((HOST,PORT))
s.listen(2)

words=["kaktus","hanskar","reiknirit","forritun","vatn","eyjafjallajökull","vaðlaheiðarvegavinnuverkfærageymsluskúraútidyralyklakippuhringur"]
stafalisti = []

while True:
    c, addr = s.accept()
    ord=words[randint(0,len(words)-1)]
    ord1=""
    print(ord)
    for x in range(len(ord)):
        ord1=ord1+"_ "
    c.send(ord1.encode())
    buinn=False
    lif=5
    while lif>0 or buinn==False:
        ord2=""
        staf=c.recv(1024).decode().lower()
        stafalisti.append(staf)
        print(stafalisti)
        if staf in ord:
            for x in ord:
                if x==staf:
                    print("sælir")
        else:
            print("haha XD")
            lif-=1
        c.send(str(lif).encode())

        """ord1 = ""
        print(staf)
        for x in ord:
            if x == staf:
                ord1=ord1+"%s " %staf
            else:
                ord1=ord1+"_ """""
        for x in ord:
            if x in stafalisti:
                for i in stafalisti:
                    if x == i:
                        ord2 += x + " "
            else:
                ord2 += "_ "
        c.send(ord2.encode())
        print(ord2)
