import tkinter as tk
import subprocess
import socket

sp = subprocess.Popen(["python", "server.py"])

def retryProgram():
    sp = subprocess.Popen(["python", "server.py"])
    executeProgram()

def executeProgram():
    for widget in root.winfo_children():
        widget.destroy()
    
    def sendResult():
        result = entry.get()
        clientScript(result)

    inputLabel=tk.Label(root, text="Please enter a non-zero integer between –121 and 121 ", font =("Arial",18))
    inputLabel.pack(pady=10)
    
    entry = tk.Entry(root, font=("Arial",32))
    entry.pack(pady=10)

    submitButton = tk.Button(root, text="Submit", command=sendResult)
    submitButton.pack(pady=5)

    output = tk.Label(root, text="",font=("Arial",18))
    output.pack(pady=10)

    retryButton = tk.Button(root, text="Retry Program", font=('Arial',18),height=5,width=15, command=retryProgram)
    retryButton.place(relx=0.0,rely=1.0,anchor="sw")

    returnButton = tk.Button(root, text="Return to OverView", font=('Arial',18),height=5,width=15, command=mainPage)
    returnButton.place(relx=0.5,rely=1.0,anchor="s")

    exitButton = tk.Button(root, text="Exit Program", font=('Arial', 18),height=5,width=15, command=root.quit)
    exitButton.place(relx=1.0,rely=1.0,anchor="se")

    clientScript()


def clientScript(ses):
    
    HOST = "127.0.0.1"
    PORT = 8080

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST,PORT))
        num = int(ses)
        if num < -121 or num > 121:
            output = tk.Label(root, text = "Error: cannot enter anything less than -121 or greater than 121.", font=("Arial", 18))
        else:
            s.sendall(ses.encode())
            data = s.recv(1024)
            output = tk.Label(root, text=f"{data.decode()}",font=("Arial",18))
    
    output.pack(pady=10)
    

def mainPage():
    for widget in root.winfo_children():
        widget.destroy()

    label = tk.Label(root, text="Project 3 Presentation", font =('Arial', 18))
    label.pack()

    label = tk.Label(root, text="Overview", font =('Arial', 18))
    label.pack()

    label = tk.Label(root, text=
                     """
We assume that the sending node sends integer values to the receiving node. First, the sender encodes the integer it wants to send using a special encoding scheme, which can be described as follows:\n
An integer value, denoted by N, is a non-zero integer between –121 and 121. The sender produces a decomposition of an integer value using powers of 3, namely 1 (or 3^0 ), 3 (or 3^1 ), 9 (or 3^2), 27 (or 3^3), and 81 (or 3^4).\n
The sender sends a sequence of –1, 0, and/or 1, each of which is associated with a power of 3. The receiver decodes the received sequence of –1, 0, and/or 1 to obtain the same value sent by the sender.\n
Constraint: Each power of 3 (i.e., 1, 3, 9, 27, and 81) should appear exactly once in the decomposition and is preceded by a coefficient, which can be –1, 0, or 1.\n
EXAMPLE: N = –3 = 0 × 81 + 0 × 27 + 0 × 9 – 1 × 3 + 0 × 1 \n
Code sent: (0, 0, 0, –1, 0) \n
To exit the program, click "Exit Program". \n
                     """,font=('Arial',14),wraplength=800,justify="center")
    label.pack(padx=10,pady=10)


    beginButton = tk.Button(root, text="Begin Program", font=('Arial', 18), height=5,width=15, command= executeProgram)
    beginButton.place(relx=0.0,rely=1.0,anchor="sw")

    exitButton = tk.Button(root, text="Exit", font=('Arial', 18),height=5,width=15, command=root.quit)
    exitButton.place(relx=1.0,rely=1.0,anchor="se")

root = tk.Tk()
root.geometry("900x700")
root.title("Project 3")

mainPage()

root.mainloop()

sp.terminate()
