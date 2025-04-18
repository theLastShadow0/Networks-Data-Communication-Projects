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

    inputLabel=tk.Label(root, text="Please enter a sequence of only T, A, or M characters ending with a #: ", font =("Arial",18))
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


def clientScript(TAM):
    
    HOST = "127.0.0.1"
    PORT = 8080

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST,PORT))

        if TAM == '#':
            output=tk.Label(root, text = "The input is empty.\n Press 'Retry Program' to start again.", font=("Arial",18))
            output.pack(pady=10)
        elif " " in TAM:
            output=tk.Label(root, text = "No spaced allowed.\n Press 'Retry Program' to start again.", font=("Arial",18))
            output.pack(pady=10)
        else:
            s.sendall(TAM.encode())
            data = s.recv(1024)

    output = tk.Label(root, text=f"The sorted sequence is: {data.decode()}",font=("Arial",18))
    output.pack(pady=10)
    

def mainPage():
    for widget in root.winfo_children():
        widget.destroy()

    label = tk.Label(root, text="Project 1 Presentation", font =('Arial', 18))
    label.pack()

    label = tk.Label(root, text="Overview", font =('Arial', 18))
    label.pack()

    label = tk.Label(root, text="""
    When you launch the application, click on "Begin Program" to enter the main screen where you'll provide your input.\n
    On the input screen, you will be prompted to enter a string consisting only of the characters 'T', 'A', and 'M', ending with a '#' symbol (e.g., "TAM#").\n
    Once you've entered the string, click "Submit" to send the input to the server.\n
    The client application sends your input string to the server over a network connection.\n
    The server receives the string, processes it by sorting the 'T's, 'A's, and 'M's, and returns the sorted string.\n
    The sorted string is displayed on the screen as the output (e.g., TTTAAAM#).\n
    If you want to try again with a different input, you can click "Retry Program".\n
    To exit the program, click "Exit Program".""", font=('Arial',14),wraplength=800,justify="center")
    label.pack(padx=10,pady=10)


    beginButton = tk.Button(root, text="Begin Program", font=('Arial', 18), height=5,width=15, command= executeProgram)
    beginButton.place(relx=0.0,rely=1.0,anchor="sw")

    exitButton = tk.Button(root, text="Exit", font=('Arial', 18),height=5,width=15, command=root.quit)
    exitButton.place(relx=1.0,rely=1.0,anchor="se")

root = tk.Tk()
root.geometry("900x700")
root.title("Project 1")

mainPage()

root.mainloop()

sp = subprocess.terminate()
