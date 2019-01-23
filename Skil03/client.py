#Kolbeinn, Ágúst, Bjarki
#Skilaverkefni 3
import socket
import pickle
import os

HOST = '10.220.226.55'
PORT = 12345

while True:
    s = socket.socket()
    s.connect((HOST, PORT))
    strengur1 = s.recv(1024)
    tries = 5
    while tries >= 0:
        print(strengur1.decode())
        stafur = input("Sláðu inn staf: ").encode()
        s.send(stafur)
    s.close()



