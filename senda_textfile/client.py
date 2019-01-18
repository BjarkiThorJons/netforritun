import socket
import pickle

#HOST = socket.gethostname()
HOST = '10.220.226.55'
PORT = 12345


s = socket.socket()
s.connect((HOST,PORT))

list = pickle.loads(s.recv(1024))
for x in range(len(list)):
    print(x+1, list[x])
numer = int(input("Veldu uppskrift með tölu: "))
s.send(pickle.dumps(numer))
f = open(list[numer-1],'wb')
data = s.recv(1024)
f.write(data)
f.close()
