import tkinter as tk
from tkinter import messagebox
import string

ALPHABET = string.ascii_lowercase
INVALID_A = {2,4,6,8,10,12,13,14,16,18,20,22,24}

def modinv(a: int, m: int) -> int:
    a %= m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    raise ValueError(f"No modular inverse for A={a} under mod {m}")

def encrypt_text(text: str, A: int, B: int) -> str:
    result = []
    for ch in text:
        if ch in ALPHABET:
            X = ALPHABET.index(ch)
            result.append(ALPHABET[(A*X + B) % 26])
        else:
            result.append(ch)
    return "".join(result)

def decrypt_text(text: str, A: int, B: int) -> str:
    invA = modinv(A, 26)
    result = []
    for ch in text:
        if ch in ALPHABET:
            X = ALPHABET.index(ch)
            result.append(ALPHABET[((X - B) * invA) % 26])
        else:
            result.append(ch)
    return "".join(result)

class AffineCipherGUI:
    def __init__(self, root):
        self.root = root
        root.title("Affine Cipher")

        # Configure grid weights for responsiveness
        for i in range(4):
            root.columnconfigure(i, weight=1)
        for i in range(5):
            root.rowconfigure(i, weight=1)

        # Key inputs
        tk.Label(root, text="Key A:", anchor="e").grid(row=0, column=0, sticky="e", padx=10, pady=10)
        self.entryA = tk.Entry(root)
        self.entryA.grid(row=0, column=1, sticky="we", padx=10, pady=10)

        tk.Label(root, text="Key B:", anchor="e").grid(row=0, column=2, sticky="e", padx=10, pady=10)
        self.entryB = tk.Entry(root)
        self.entryB.grid(row=0, column=3, sticky="we", padx=10, pady=10)

        # Input text
        tk.Label(root, text="Input Text:", anchor="nw").grid(row=1, column=0, sticky="nw", padx=10, pady=5)
        self.text_input = tk.Text(root)
        self.text_input.grid(row=1, column=1, columnspan=3, sticky="nsew", padx=10, pady=5)

        # Buttons
        self.encrypt_btn = tk.Button(root, text="Encrypt", command=self.encrypt_action)
        self.encrypt_btn.grid(row=2, column=1, sticky="ew", padx=10, pady=5)

        self.decrypt_btn = tk.Button(root, text="Decrypt", command=self.decrypt_action)
        self.decrypt_btn.grid(row=2, column=2, sticky="ew", padx=10, pady=5)

        # Output text
        tk.Label(root, text="Output Text:", anchor="nw").grid(row=3, column=0, sticky="nw", padx=10, pady=5)
        self.text_output = tk.Text(root, state="normal")
        self.text_output.grid(row=3, column=1, columnspan=3, sticky="nsew", padx=10, pady=5)

    def get_keys(self):
        try:
            A = int(self.entryA.get())
            B = int(self.entryB.get())
        except ValueError:
            messagebox.showerror("Invalid Key", "A and B must be integers.")
            return None, None
        if A in INVALID_A:
            messagebox.showerror("Invalid Key", "Key A must be coprime with 26.")
            return None, None
        return A, B

    def encrypt_action(self):
        A, B = self.get_keys()
        if A is None: return
        txt = self.text_input.get("1.0", tk.END).strip().lower()
        result = encrypt_text(txt, A, B)
        self.text_output.config(state="normal")
        self.text_output.delete("1.0", tk.END)
        self.text_output.insert(tk.END, result)
        self.text_output.config(state="disabled")

    def decrypt_action(self):
        A, B = self.get_keys()
        if A is None: return
        txt = self.text_input.get("1.0", tk.END).strip().lower()
        try:
            result = decrypt_text(txt, A, B)
        except ValueError as e:
            messagebox.showerror("Error", str(e))
            return
        self.text_output.config(state="normal")
        self.text_output.delete("1.0", tk.END)
        self.text_output.insert(tk.END, result)
        self.text_output.config(state="disabled")

if __name__ == "__main__":
    root = tk.Tk()
    # Maximize or fullscreen
    try:
        root.state('zoomed')
    except:
        root.attributes('-fullscreen', True)
    AffineCipherGUI(root)
    root.mainloop()