# importin okkar
import socket
from _thread import *
import threading 

#læis threadnum
print_lock = threading.Lock() 
  
# bý til thread fall
def threaded(c): 
    while True:
  
        # fæ gögn frá notanda
        data = c.recv(1024) 
        if not data: 
            print('Bye') 
              
            # opna threadið þegar lokað er á connectionið
            print_lock.release()
            break

        # sný strengnum frá notanda við
        data = data[::-1]

        # sendi notanda strenginn til baka
        c.send(data)

    c.close()

  
def Main(): 
    host = ""
    port = 12345
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    s.bind((host, port)) 
    print("socket binded to post", port) 
  
    # lætur socketið hlusta vel :)
    s.listen(5) 
    print("socket is listening") 

    while True: 
  
        # ná sambandi við client
        c, addr = s.accept() 

        # lás fengin af client
        print_lock.acquire() 
        print('Connected to :', addr[0], ':', addr[1]) 

        # Bý til nýjan þráð og skila identifier þráðsins
        start_new_thread(threaded, (c,)) 
    s.close() 
  
  
if __name__ == '__main__': 
    Main()
