import socket
ss=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ss.bind("127.0.0.1",6677)
ss.listen()

c1,cAdd = ss.accept()

clientAddress = cAdd[0]
clientPort = cAdd[1]