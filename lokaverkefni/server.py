import socket
import _thread


HOST = socket.gethostname()
PORT = 12345

s = socket.socket()
s.bind((HOST,PORT))
s.listen(2)
c, addr = s.accept()

def sendaSkilabod(skilabod):
    try:
        c.send(skilabod.encode())
    except:
        pass
def faSkilabod():
    while True:
        try:
            print("\n",c.recv(1024).decode())
        except:
            pass
_thread.start_new_thread( faSkilabod, () )
while True:
    _thread.start_new_thread( sendaSkilabod, (input("Sláðu inn: "),) )
   

