import socket

cs=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
cs.connect(("127.0.0.1",6677))

while True:
    input("Press Enter to send request\n")
    print(
    "1. Request list of files currently available on the server .\n"
    "2. Select a file to be copied to the client side.\n"
    "3.Quit\n"
      )
    option = input("Select request: ")
    if option == 1:
        query = "list"
    if option == 2:
        query = input("\nEnter file name: ")