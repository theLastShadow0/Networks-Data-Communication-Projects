import tkinter as tk
import numpy as np
from matplotlib.figure import Figure
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

        NRZ = binary_input
        NRZI = NRZI_encoding(binary_input)
        manchester = manchester_encoding(binary_input)

        x_nrz = np.arange(len(NRZ))
        x_clock = np.arange(0, len(binary_input), 0.5)
        x_nrzi = np.arange(len(NRZI)) + 0.5
        x_manchester = np.arange(0, len(manchester), 0.5)

        fig = Figure(figsize=(6,8))
        ax1 = fig.add_subplot(4, 1, 1)
        ax2 = fig.add_subplot(4, 1, 2)
        ax3 = fig.add_subplot(4, 1, 3)
        ax4 = fig.add_subplot(4, 1, 4)

        ax1.step(x_nrz, [int(bit) for bit in NRZ], where='post', label="NRZ")
        ax1.set_title("NRZ")
        ax1.set_xticks(x_nrz)
        ax1.set_xticklabels([(bit) for bit in NRZ])
        ax1.grid(True)

        ax2.step(x_clock, np.tile([0, 1], len(binary_input)), where='post', label="Clock")
        ax2.set_title("Clock")
        ax2.set_xticks(x_clock)
        ax2.set_xticklabels(np.tile([0, 1], len(binary_input)))
        ax2.grid(True)

        ax3.step(x_manchester, [int(bit) for bit in manchester for _ in range(2)], where='post', label="Manchester")
        ax3.set_title("Manchester")
        ax3.set_xticks(x_manchester)
        ax3.set_xticklabels([(bit) for bit in manchester for _ in range(2)])
        ax3.grid(True)

        ax4.step(x_nrzi, [(bit) for bit in NRZI], where='post', label="NRZI")
        ax4.set_title("NRZI")
        ax4.set_xticks(np.arange(len(binary_input)))
        ax4.set_xticklabels([(bit) for bit in NRZI])
        ax4.grid(True)

        fig.subplots_adjust(hspace=1.0)

        canvas = FigureCanvasTkAgg(fig, master=root)
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.NONE, expand=False)
        canvas.get_tk_widget().config(width=2000, height=500)
        canvas.draw()

        
    
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