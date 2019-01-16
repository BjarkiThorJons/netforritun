import socket

HOST = socket.gethostname()
PORT = 12345

#with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
s = socket.socket()
s.bind((HOST,PORT))
s.listen(2)
c, addr = s.accept()
#with conn:
while True:
    f = open('s.txt','rb')
    c, addr = s.accept()
    #data = c.recv(1024)
    print('Connected by', addr)
    #c.send(b'Hi')
    #data = c.recv(1024)
    #print(data)
    data = f.read(1024)
    c.send(data)
    f.close()
    #if not data:
         #break

