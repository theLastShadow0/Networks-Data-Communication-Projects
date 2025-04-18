#Client

import socket

HOST = "127.0.0.1"
PORT = 8080

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST,PORT))
    TAM = input("Please enter a sequence of only T, A, or M characters ending with a #: ")

    if TAM == '#':
        print("The input is empty try again.")
    else:
        s.sendall(TAM.encode())
        data = s.recv(1024)

print(f"The sorted sequence is: {data.decode()}")