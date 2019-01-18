#Kolbeinn, Ágúst, Bjarki
#Skilaverkefni 2
import socket
import pickle
from os import listdir
from os.path import isfile, join
from re import *

HOST = '10.220.226.55'
PORT = 12345

while True:

    s = socket.socket()
    s.connect((HOST, PORT))
    while True:
        onlyfiles = [f for f in listdir("./") if (isfile(join("./", f)) and match(".*.txt", f))]
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
            for x in range(len(onlyfiles)):
                print(x+1, onlyfiles[x])

            numer = int(input("Veldu númer: "))
            f = open(onlyfiles[numer-1], "rb")
            s.send(pickle.dumps(onlyfiles[numer-1]))
            data = f.read(1024)
            s.send(data)
            f.close()
            break
    s.close()



