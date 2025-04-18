#Server
import socket

def SWAP_Server(TAM_TAB_Server, i, j):
    if i != j:
        temp = TAM_TAB_Server[i]
        TAM_TAB_Server[i] = TAM_TAB_Server[j]
        TAM_TAB_Server[j] = temp

def Sort_TAM_Server(TAM_TAB_Server):
    TAM_TAB_Server = list(TAM_TAB_Server)
    low = 0
    mid = 0
    high = len(TAM_TAB_Server) - 2
    while mid <= high:
        if TAM_TAB_Server[mid] == 'T':
            SWAP_Server(TAM_TAB_Server, low, mid)
            low += 1
            mid += 1
        elif TAM_TAB_Server[mid] == 'A':
            mid += 1
        elif TAM_TAB_Server[mid] == 'M':
            SWAP_Server(TAM_TAB_Server, mid, high)
            high -= 1
    TAM_TAB_Server = "".join(TAM_TAB_Server)
    TAM_TAB_Server = TAM_TAB_Server.rstrip("#")
    return TAM_TAB_Server
#Listening Socket

HOST = "127.0.0.1"
PORT = 8080

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST,PORT))
    s.listen()
    print('Server is waiting for a client connection...')
    conn, addr = s.accept()

#Exchange of Data

with conn:
    print(f"Successfully connected with client address: {addr}")
    while True:
        data = conn.recv(1024)
        if not data:
            break

        data_str = data.decode()
        sorted_data = Sort_TAM_Server(data_str)
        conn.sendall(sorted_data.encode())
        print('Message Sent.')

