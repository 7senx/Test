import socket

ss=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
ss.bind(("127.0.0.1",5522))

