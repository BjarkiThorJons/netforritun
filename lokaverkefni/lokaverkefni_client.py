import socket
import _thread as t
import time

s = socket.socket()

HOST = "10.201.94.217"
PORT = 12345

s.connect((HOST, PORT))


def faSkilabod():
    while True:
        try:
            print("\n", s.recv(1024).decode())
        except:
            print("unable to recieve")


def senda(skilabod):
    try:
        s.send(skilabod.encode())
    except:
        print("unable to send")


t.start_new_thread(faSkilabod, ())

while True:
    t.start_new_thread(senda, (input("Texti:"),))
