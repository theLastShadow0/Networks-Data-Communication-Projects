#Client

import socket

HOST = "127.0.0.1"
PORT = 8080

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST,PORT))
    ses = input("Please enter a non-zero integer between –121 and 121 ")

    num  = int(ses)
    if num < -121 or num > 121:
        print("Error: cannot enter anything less than -121 or greater than 121.")
    else:
        s.sendall(ses.encode())
        data = s.recv(1024)
        print(f"The answer is: {data.decode()}")
