import socket

host = '10.220.226.55'

# portið er skilgreint
port = 12345

# búum til socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# hér tengjumst við servernum
s.connect((host, port))

# hér er messagið sjálft sem við sendum
message = "saelir boisar"
while True:

    # sendum message með ascci encoding
    s.send(message.encode('ascii'))

    # fáum message og skýrum það data
    data = s.recv(1024)

    # prenta messagið í
    # það ætti að vera öfugt hérna
    print('Received from the server :', str(data.decode('ascii')))

    # input sem spyr notanda hvort hann vill halda áfram
    ans = input('\nDo you want to continue(y/n) :')
    if ans == 'y':
        continue
    else:
        break
# lokum tengingunni
s.close()
