import socket

# create, connect, send/receive, close

clientS = socket.socket()

serverIP = "localhost"
serverPort = 5510

clientS.connect((serverIP, serverPort))

print("Connection established...")

data = clientS.recv(1024)

while data:
    print("Received from server:",data.decode())
    msg = input("Enter message or EXIT")
    if msg!='EXIT':
        clientS.send(msg.encode())
    else:
        break
    data = clientS.recv(1024)

clientS.close()
print("Connection closed...")
