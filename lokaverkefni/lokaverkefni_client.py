import socket
import _thread as t
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import os
import time


s = socket.socket()

HOST = "10.201.95.80"
PORT = 12345

s.connect((HOST, PORT))



def faSkilabod():
    while True:
        try:
            skilabod = s.recv(1024).decode()
            if skilabod == "file":
                nafn_size = s.recv(1024).decode() #nafnið a file-inu
                listi = nafn_size.split(",")
                filesize = int(listi[1])
                nafn = listi[0]
                with open(nafn, "wb") as f:
                    data = s.recv(filesize)
                    f.write(data)
                    print("\nFile recieved")
                    print("Texti:")
                os.system(nafn)

            elif skilabod == "texti":
                print("\n", s.recv(1024).decode())
                print("Texti:", end="")
        except:
            print("unable to recieve")


def senda(skilabod):
    try:
    #skilabod = input("Texti:")
    #if True:
        if skilabod:
            if skilabod[0] == "/":
                if "file" in skilabod:
                    s.send("file".encode()) # láta client vita að hann sé að recieva file
                    filename = askopenfilename() #veljum file
                    f = open(filename, "rb")
                    nafn = filename.split("/")[-1] + "," + str(os.path.getsize(filename))
                    s.send(nafn.encode()) #senda nafnið a file-inu
                    skilabod = f.read()
                    f.close()
                    s.send(skilabod)
            else:
                s.send("texti".encode())
                s.send(skilabod.encode())
    except:
        print("unable to send")


t.start_new_thread(faSkilabod, ())
while True:
    senda(input("Texti:"))

