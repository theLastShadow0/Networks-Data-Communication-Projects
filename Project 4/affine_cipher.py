import tkinter as tk
from tkinter import messagebox
import string
import platform

ALPHABET = string.ascii_lowercase
INVALID_A = {2,4,6,8,10,12,13,14,16,18,20,22,24}

def modinv(a: int, m: int) -> int:
    a %= m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    raise ValueError(f"No modular inverse for A={a} under mod {m}")

class AffineCipherGUI:
    def __init__(self, root):
        self.root = root
        root.title("Affine Cipher")
        # Fullscreen
        try:
            root.state('zoomed')
        except:
            root.attributes('-fullscreen', True)

        # Overview frame
        self.overview_frame = tk.Frame(root)
        self.overview_frame.pack(fill="both", expand=True)
        overview_text = (
            "Project 2 (Affine Cipher):\n"
            "The affine cipher is a substitution cipher, where a plaintext letter x is\n"
            "enciphered into a ciphertext letter y as follows:\n\n"
            "    y = αx + β (mod 26)\n\n"
            "The key for this encryption function is (α, β), where 0 ≤ α, β ≤ 25.\n"
            "There are 12 possible choices for α with gcd(α, 26) = 1, and 26 choices for β.\n"
            "Thus, there are 12×26 = 312 choices for the key.\n\n"
            "The decryption is accomplished by:\n\n"
            "    x = α⁻¹ (y − β) (mod 26),\n"
            "where α⁻¹ is the modular inverse of α.\n\n"
            "1. Write an algorithm for the affine cipher.\n"
            "2. Show that your proposed algorithm is correct (informal proof).\n"
            "3. Provide a program simulating this cipher, displaying ciphertext,\n"
            "   plaintext, and key, with step-by-step details."
        )
        lbl = tk.Label(self.overview_frame, text=overview_text, justify="left", font=("Arial", 20))
        lbl.pack(fill="both", expand=True)

        btn_start = tk.Button(self.overview_frame, text="Begin", command=self.show_main,font=("Arial", 30))
        btn_start.pack()

        # Main frame
        self.main_frame = tk.Frame(root)
        for i in range(4):
            self.main_frame.columnconfigure(i, weight=0)
        for i in range(6):
            self.main_frame.rowconfigure(i, weight=0)

        tk.Label(self.main_frame, text="Key A:").grid(row=0, column=0, sticky="e")
        self.entryA = tk.Entry(self.main_frame,font=("Arial",20))
        self.entryA.grid(row=0, column=1, sticky="we")

        tk.Label(self.main_frame, text="Key B:").grid(row=0, column=2, sticky="e")
        self.entryB = tk.Entry(self.main_frame,font=("Arial",20))
        self.entryB.grid(row=0, column=3, sticky="we")

        tk.Label(self.main_frame, text="Input:").grid(row=1, column=0, sticky="n")
        self.text_input = tk.Text(self.main_frame, height=5, width=40, font=("Arial",20))
        self.text_input.grid(row=1, column=1, columnspan=3, sticky="w")

        self.encrypt_btn = tk.Button(self.main_frame, text="Encrypt", command=self.encrypt_action,font=("Arial",20),bg="green", fg="white")
        self.encrypt_btn.grid(row=2, column=1, sticky="ew")

        self.decrypt_btn = tk.Button(self.main_frame, text="Decrypt", command=self.decrypt_action,font=("Arial",20),bg="red", fg="white")
        self.decrypt_btn.grid(row=2, column=2, sticky="ew")

        tk.Label(self.main_frame, text="Output:").grid(row=3, column=0, sticky="n")
        self.text_output = tk.Text(self.main_frame, state="disabled",height=5, width=40, font=("Arial",20))
        self.text_output.grid(row=3, column=1, columnspan=3, sticky="w")

        tk.Label(self.main_frame, text="Steps:").grid(row=4, column=0, sticky="n")
        self.text_log = tk.Text(self.main_frame, state="disabled", width=40, font=("Arial",20))
        self.text_log.grid(row=4, column=1, columnspan=3, sticky="w")

    def show_main(self):
        self.overview_frame.pack_forget()
        self.main_frame.pack(fill="both", expand=True)

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
        self.text_output.config(state="normal"); self.text_output.delete("1.0", tk.END)
        self.text_log.config(state="normal");   self.text_log.delete("1.0", tk.END)
        for ch in self.text_input.get("1.0", tk.END).strip().lower():
            if ch in ALPHABET:
                X = ALPHABET.index(ch)
                C = (A*X + B) % 26
                cipher_char = ALPHABET[C]
                self.text_log.insert(tk.END, f"{A}*{X}({ch})+{B} mod26={C}({cipher_char})\n")
                self.text_output.insert(tk.END, cipher_char)
            else:
                self.text_output.insert(tk.END, ch)
        self.text_output.config(state="disabled"); self.text_log.config(state="disabled")

    def decrypt_action(self):
        A, B = self.get_keys()
        if A is None: return
        self.text_output.config(state="normal"); self.text_output.delete("1.0", tk.END)
        self.text_log.config(state="normal");   self.text_log.delete("1.0", tk.END)
        try:
            invA = modinv(A, 26)
        except ValueError as e:
            messagebox.showerror("Error", str(e)); return
        for ch in self.text_input.get("1.0", tk.END).strip().lower():
            if ch in ALPHABET:
                X = ALPHABET.index(ch)
                P = ((X - B) * invA) % 26
                plain_char = ALPHABET[P]
                self.text_log.insert(tk.END, f"({X}({ch})-{B})*{invA} mod26={P}({plain_char})\n")
                self.text_output.insert(tk.END, plain_char)
            else:
                self.text_output.insert(tk.END, ch)
        self.text_output.config(state="disabled"); self.text_log.config(state="disabled")

if __name__ == "__main__":
    root = tk.Tk()
    AffineCipherGUI(root)
    root.mainloop()