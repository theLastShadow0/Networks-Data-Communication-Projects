#Client

import socket

HOST = "127.0.0.1"
PORT = 8080

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST,PORT))
    ses = input("Please enter a non-zero integer between –121 and 121 ")

    if ses == '0':
        print("cannot enter 0.")
    else:
        s.sendall(ses.encode())
        data = s.recv(1024)

print(f"The answer is: {data.decode()}")