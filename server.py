import socket

# create, bind, listen, accept, send/receive, close

listenS = socket.socket()

ip = "localhost"
port = 5510

listenS.bind((ip, port))

listenS.listen(1) # Server is capable of serving one client at a time

print("Server started listening on port...",port)
dataS, clientAddr = listenS.accept()

print("Connection request received from...",clientAddr)

dataS.send("Hello Client...".encode())

reply = dataS.recv(1024)

while reply:
    print("Received from client:", reply.decode())
    msg = input("Enter message or EXIT")
    if msg!='EXIT':
        dataS.send(msg.encode())
    else:
        break
    reply = dataS.recv(1024)

dataS.close()
print("Client connection is closed...")
listenS.close()
print("Server shutdown...")
