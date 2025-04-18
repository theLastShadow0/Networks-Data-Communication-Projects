import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg)

def retryProgram():
    executeProgram()

def NRZI_encoding(binary_seq):
    binary_seq = list(binary_seq)  
    count = 0  

    def skip_bit(count):
        if count < len(binary_seq) and binary_seq[count] == '1':  #if it starts at 1 increment count and go to while loop
            count += 1
            switch_bit(count)

        elif count < len(binary_seq) and binary_seq[count] =='0': #if it starts at 0 increment count and repeat skip_bit function
            count += 1
            skip_bit(count)

    def switch_bit(count):
        while count < len(binary_seq):

            if binary_seq[count] == '0':
                binary_seq[count] = '1'  

            elif binary_seq[count] == '1':
                binary_seq[count] = '0'
                count += 1
                skip_bit(count)
                break

            count += 1

    skip_bit(count)
    return "".join(binary_seq)
     
def manchester_encoding(bin_seq):
    manchester = ""
    for bit in bin_seq:
        if bit == '0':
            manchester += "01"  # Low-to-High
        else:
            manchester += "10"  # High-to-Low
    return manchester

def executeProgram():
    for widget in root.winfo_children():
        widget.destroy()


    def encoding_strategies():
        binary_input = entry.get()

        # Create a frame to hold the plots
        plot_frame = tk.Frame(root)
        plot_frame.pack(pady=10)

        # NRZ Plot
        NRZ = binary_input
        xaxis1 = np.arange(len(NRZ))
        yaxis1 = [int(bit) for bit in NRZ]

        fig, ax = plt.subplots(figsize=(3,3))
        ax.set_xlim(-1, len(binary_input))
        ax.set_title('NRZ')
        ax.step(xaxis1, yaxis1, where='post')

        ax.set_xticks(xaxis1)
        ax.set_xticklabels([bit for bit in binary_input])
        ax.set_yticks([0,1])
        ax.set_yticklabels(['0', '1'])

        canvas = FigureCanvasTkAgg(fig, master=plot_frame)
        canvas.draw()
        canvas.get_tk_widget().grid(row=0, column=0, padx=5, pady=5)  # Place in top-left

        # NRZI Plot
        NRZI = NRZI_encoding(binary_input)
        xaxis_nrzi = np.arange(len(NRZI)) + 0.5
        yaxis_nrzi = [int(bit) for bit in NRZI]

        fig, ax = plt.subplots(figsize=(3,3))
        ax.set_xlim(-1, len(binary_input))
        ax.set_title('NRZI')
        ax.step(xaxis_nrzi, yaxis_nrzi, where='post')

        ax.set_xticks(np.arange(len(binary_input)))
        ax.set_xticklabels([bit for bit in binary_input])
        ax.set_yticks([0,1])
        ax.set_yticklabels(['0', '1'])

        canvas = FigureCanvasTkAgg(fig, master=plot_frame)
        canvas.draw()
        canvas.get_tk_widget().grid(row=0, column=1, padx=5, pady=5)  # Place in top-right

        # Clock Plot
        x, y = np.arange(0, len(binary_input), 0.5), np.tile([0, 1], len(binary_input))

        fig, ax = plt.subplots(figsize=(3,3))
        ax.set_xlim(-1, len(binary_input))
        ax.set_title('Clock Signal')
        ax.step(x, y, where='post')
        ax.set_xticks(np.arange(len(binary_input)))
        ax.set_xticklabels([bit for bit in binary_input])
        ax.set_yticks([0, 1])
        ax.set_yticklabels(['0', '1'])

        canvas = FigureCanvasTkAgg(fig, master=plot_frame)
        canvas.draw()
        canvas.get_tk_widget().grid(row=1, column=0, padx=5, pady=5)  # Place in bottom-left

        # Manchester Plot
        manchester = manchester_encoding(NRZ)
        xman = np.arange(0, len(manchester), 0.5)
        yman = [int(bit) for bit in manchester for _ in range(2)]

        fig, ax = plt.subplots(figsize=(3,3))
        ax.step(xman,yman,where='post')
        ax.set_title('Manchester')
        ax.set_xlim(-1, len(manchester))
        ax.set_yticks([0, 1])
        ax.set_yticklabels(['0', '1'])

        ax.set_xticks(np.arange(0, len(manchester), 2))
        ax.set_xticklabels([bit for bit in NRZ])

        canvas = FigureCanvasTkAgg(fig, master=plot_frame)
        canvas.draw()
        canvas.get_tk_widget().grid(row=1, column=1, padx=5, pady=5)
    
    inputLabel=tk.Label(root, text="Please enter a binary sequence: ", font =("Arial",18))
    inputLabel.pack(pady=10)
    
    entry = tk.Entry(root, font=("Arial",30))
    entry.pack(pady=10)

    submitButton = tk.Button(root, text="Submit", command=encoding_strategies)
    submitButton.pack(pady=5)

    retryButton = tk.Button(root, text="Retry Program", font=('Arial',18),height=5,width=15, command=retryProgram)
    retryButton.place(relx=0.0,rely=1.0,anchor="sw")

    returnButton = tk.Button(root, text="Return to OverView", font=('Arial',18),height=5,width=15, command=mainPage)
    returnButton.place(relx=0.5,rely=1.0,anchor="s")

    exitButton = tk.Button(root, text="Exit Program", font=('Arial', 18),height=5,width=15, command=root.quit)
    exitButton.place(relx=1.0,rely=1.0,anchor="se")

def mainPage():
    for widget in root.winfo_children():
        widget.destroy()

    label = tk.Label(root, text="Project 2 Presentation", font =('Arial', 18))
    label.pack()

    label = tk.Label(root, text="Overview", font =('Arial', 18))
    label.pack()

    label = tk.Label(root, text="""
    When you launch the application, click on "Begin Program" to enter the main screen where you'll provide your input.\n
    On the input screen, you will be asked to input a binary sequence. Enter a binary sequence of only characters '1's and '0's.\n
    After entering your binary sequence, click the submit button.\n
    You will then be shown the 3 different encoding strategies such as:\n
    NRZ, NRZI, and Manchester encodings alongside the clock sequence.\n
    If you want to try again with a different input, you can click "Retry Program".\n
    To exit the program, click "Exit Program".""", font=('Arial',14),wraplength=800,justify="center")
    label.pack(padx=10,pady=10)


    beginButton = tk.Button(root, text="Begin Program", font=('Arial', 18), height=5,width=15, command= executeProgram)
    beginButton.place(relx=0.0,rely=1.0,anchor="sw")

    exitButton = tk.Button(root, text="Exit", font=('Arial', 18),height=5,width=15, command=root.quit)
    exitButton.place(relx=1.0,rely=1.0,anchor="se")

root = tk.Tk()
root.geometry("900x700") 
root.title("Project 2")

mainPage()

root.mainloop()