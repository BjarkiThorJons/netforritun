#Kolbeinn, Ágúst, Bjarki
#Skilaverkefni 2
import socket
import pickle
from os import listdir
import os
from os.path import isfile, join
from re import *
from tkinter import Tk
from tkinter.filedialog import askopenfilename

HOST = '10.201.94.238'
PORT = 12345

Tk().withdraw()# we don't want a full GUI, so keep the root window from appearing

while True:
    s = socket.socket()
    s.connect((HOST, PORT))
    while True:
        onlyfiles = [f for f in listdir("./") if (isfile(join("./", f)) and match(".*", f))]
        print("\n1. Fá file")
        print("2. Senda file")
        val = int(input("Veldu númer: "))
        s.send(pickle.dumps(val))

        if val == 1:
            data = pickle.loads(s.recv(1024))
            for x in range(len(data)):
                print(x+1, data[x])

            numer = int(input("Veldu númer: "))
            s.send(pickle.dumps(numer))
            f = open(data[numer-1], 'wb')
            data = s.recv(1024)
            f.write(data)
            f.close()
            break

        elif val == 2:
            """for x in range(len(onlyfiles)):
                print(x+1, onlyfiles[x])

            numer = int(input("Veldu númer: "))
            osCommandString = "%s" % onlyfiles[numer-1]
            os.system(osCommandString)
            """
            filename = askopenfilename()# show an "Open" dialog box and return the path to the selected file
            f = open(filename, "rb")
            print(filename)
            print(filename.split("/")[-1])
            s.send(pickle.dumps(["benni.mp4", os.path.getsize(filename)]))
            data = f.read()
            s.send(data)
            f.close()
            break
    s.close()
