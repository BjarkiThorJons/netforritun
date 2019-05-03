import socket
import _thread
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import os
HOST = socket.gethostname()
PORT = 12345

s = socket.socket()
s.bind((HOST,PORT))
s.listen(2)
c, addr = s.accept()
def faSkilabod():
    while True:
        try:
            skilabod = c.recv(1024).decode()
            if skilabod == "file":
                listi = c.recv(1024).decode()
                listi = listi.split(",")
                filesize = int(listi[1])
                nafn = listi[0]
                with open(nafn,"wb") as f:
                    data = c.recv(filesize)
                    f.write(data)
                    print("\nFile recieved")
                    print("Texti: ")
                os.system(nafn)
            elif skilabod == "texti":
                print("\n",c.recv(1024).decode())
                print("Texti:",end="")
        except:
            print("recieve error")


def sendaSkilabod(skilabod):
    try:
        if skilabod:
            if skilabod[0]== "/":
                if "file" in skilabod:
                    c.send("file".encode())
                    filename = askopenfilename()
                    f = open(filename,"rb")
                    nafn = filename.split("/")[-1] + ","+str(os.path.getsize(filename))
                    c.send(nafn.encode())
                    skilabod = f.read()
                    f.close()
                    c.send(skilabod)
            else:
                c.send("texti".encode())
                c.send(skilabod.encode())
    except:
        print("send error")

_thread.start_new_thread( faSkilabod, () )
while True:
     sendaSkilabod(input("Texti: "))
