import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    length = int(length_entry.get())
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    password_var.set(password)
    check_strength(password)

def check_strength(password):
    strength = "Weak ❌"
    if len(password) >= 8:
        strength = "Medium ⚠️"
    if len(password) >= 12 and any(c.isdigit() for c in password) and any(c in string.punctuation for c in password):
        strength = "Strong ✅"
    strength_var.set(strength)

def copy_password():
    root.clipboard_clear()
    root.clipboard_append(password_var.get())
    messagebox.showinfo("Copied", "Password copied!")

root = tk.Tk()
root.title("Password Generator Pro")
root.geometry("400x300")

tk.Label(root, text="Password Length").pack()
length_entry = tk.Entry(root)
length_entry.pack()

tk.Button(root, text="Generate Password", command=generate_password).pack(pady=10)

password_var = tk.StringVar()
tk.Entry(root, textvariable=password_var, width=30).pack()

strength_var = tk.StringVar()
tk.Label(root, textvariable=strength_var).pack(pady=5)

tk.Button(root, text="Copy 📋", command=copy_password).pack(pady=10)

root.mainloop()
