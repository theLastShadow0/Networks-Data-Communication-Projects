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

class AffineCipherGUI:
    def __init__(self, root):
        self.root = root
        root.title("Affine Cipher")

        # Fullscreen / maximized
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
        lbl = tk.Label(self.overview_frame, text=overview_text, justify="left", font=("Arial", 14))
        lbl.pack(padx=20, pady=20, expand=True)

        btn_start = tk.Button(self.overview_frame, text="Begin", font=("Arial", 16), command=self.show_main)
        btn_start.pack(pady=10)

        # Main cipher frame (hidden initially)
        self.main_frame = tk.Frame(root)

        # Configure grid
        for i in range(4):
            self.main_frame.columnconfigure(i, weight=1)
        for i in range(6):
            self.main_frame.rowconfigure(i, weight=1)

        # Key inputs
        tk.Label(self.main_frame, text="Key A:", anchor="e").grid(row=0, column=0, sticky="e", padx=5, pady=5)
        self.entryA = tk.Entry(self.main_frame)
        self.entryA.grid(row=0, column=1, sticky="we", padx=5, pady=5)

        tk.Label(self.main_frame, text="Key B:", anchor="e").grid(row=0, column=2, sticky="e", padx=5, pady=5)
        self.entryB = tk.Entry(self.main_frame)
        self.entryB.grid(row=0, column=3, sticky="we", padx=5, pady=5)

        # Input text
        tk.Label(self.main_frame, text="Input Text:", anchor="nw").grid(row=1, column=0, sticky="nw", padx=5, pady=5)
        self.text_input = tk.Text(self.main_frame)
        self.text_input.grid(row=1, column=1, columnspan=3, sticky="nsew", padx=5, pady=5)

        # Buttons
        self.encrypt_btn = tk.Button(self.main_frame, text="Encrypt", command=self.encrypt_action)
        self.encrypt_btn.grid(row=2, column=1, sticky="ew", padx=5, pady=5)

        self.decrypt_btn = tk.Button(self.main_frame, text="Decrypt", command=self.decrypt_action)
        self.decrypt_btn.grid(row=2, column=2, sticky="ew", padx=5, pady=5)

        # Output text
        tk.Label(self.main_frame, text="Output Text:", anchor="nw").grid(row=3, column=0, sticky="nw", padx=5, pady=5)
        self.text_output = tk.Text(self.main_frame, state="disabled")
        self.text_output.grid(row=3, column=1, columnspan=3, sticky="nsew", padx=5, pady=5)

        # Log of steps
        tk.Label(self.main_frame, text="Steps:", anchor="nw").grid(row=4, column=0, sticky="nw", padx=5, pady=5)
        self.text_log = tk.Text(self.main_frame, state="disabled", bg="#f0f0f0")
        self.text_log.grid(row=4, column=1, columnspan=3, sticky="nsew", padx=5, pady=5)

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
        plain = self.text_input.get("1.0", tk.END).strip().lower()
        self.text_output.config(state="normal")
        self.text_output.delete("1.0", tk.END)
        self.text_log.config(state="normal")
        self.text_log.delete("1.0", tk.END)

        for ch in plain:
            if ch in ALPHABET:
                X = ALPHABET.index(ch)
                C = (A*X + B) % 26
                cipher_char = ALPHABET[C]
                self.text_log.insert(tk.END,
                    f"{A}*{X}({ch}) + {B} mod26 = {C}({cipher_char})\n")
                self.text_output.insert(tk.END, cipher_char)
            else:
                self.text_output.insert(tk.END, ch)

        self.text_output.config(state="disabled")
        self.text_log.config(state="disabled")

    def decrypt_action(self):
        A, B = self.get_keys()
        if A is None: return
        cipher = self.text_input.get("1.0", tk.END).strip().lower()
        self.text_output.config(state="normal")
        self.text_output.delete("1.0", tk.END)
        self.text_log.config(state="normal")
        self.text_log.delete("1.0", tk.END)

        try:
            invA = modinv(A, 26)
        except ValueError as e:
            messagebox.showerror("Error", str(e))
            return

        for ch in cipher:
            if ch in ALPHABET:
                X = ALPHABET.index(ch)
                P = ((X - B) * invA) % 26
                plain_char = ALPHABET[P]
                self.text_log.insert(tk.END,
                    f"({X}({ch}) - {B})*{invA} mod26 = {P}({plain_char})\n")
                self.text_output.insert(tk.END, plain_char)
            else:
                self.text_output.insert(tk.END, ch)

        self.text_output.config(state="disabled")
        self.text_log.config(state="disabled")

if __name__ == "__main__":
    root = tk.Tk()
    app = AffineCipherGUI(root)
    root.mainloop()
