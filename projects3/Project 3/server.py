#Server
import socket

""" PROBLEM STATEMENT 

We assume that the sending node sends integer values to the receiving node. First, the sender encodes the integer it wants to send using a special encoding scheme, which can be described as follows:

An integer value, denoted by N, is a non-zero integer between –121 and 121. The sender produces a decomposition of an integer value using powers of 3, namely 1 (or 3^0 ), 3 (or 3^1 ), 9 (or 3^2), 27 (or 3^3), and 81 (or 3^4).

The sender sends a sequence of –1, 0, and/or 1, each of which is associated with a power of 3. The receiver decodes the received sequence of –1, 0, and/or 1 to obtain the same value sent by the sender.

Constraint: Each power of 3 (i.e., 1, 3, 9, 27, and 81) should appear exactly once in the decomposition and is preceded by a coefficient, which can be –1, 0, or 1.

EXAMPLE: N = –3 = –3 = 0 × 81 + 0 × 27 + 0 × 9 – 1 × 3 + 0 × 1
Code sent: (0, 0, 0, –1, 0)

 """


def special_encoding_scheme(N: int):
    powers = [81, 27, 9, 3, 1]
    nums = [0,0,0,0,0]
    for i in range(5):
        if abs(N) >= powers[i]:
            if N < 0:
                nums[i] = -1
                N = N + powers[i]
            else:
                nums[i] = 1
                N = N - powers[i]
        elif i != len(nums) - 1:
            if abs(N) > powers[i + 1]:
                if N < 0:
                    nums[i] = -1
                    N = N + powers[i]
                else:
                    nums[i] = 1
                    N = N - powers[i]
            else:
                nums[i] = 0
    return nums

print(special_encoding_scheme(-3))
print(special_encoding_scheme(7))
print(special_encoding_scheme(-5))
print(special_encoding_scheme(9))
print(special_encoding_scheme(-16))
print(special_encoding_scheme(25))
print(special_encoding_scheme(-89))
print(special_encoding_scheme(121))
print(special_encoding_scheme(-121))
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
        try:
            data_int = int(data_str)
            sorted_data = special_encoding_scheme(data_int)
            response = str(sorted_data).encode()
            conn.sendall(response)
            print('Message Sent.')
        except ValueError:
            conn.sendall(b"Invalid input. Please send an integer between -121 and 121.")
