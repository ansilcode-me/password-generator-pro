import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    username = username_entry.get()
    if username == "":
        messagebox.showwarning("Error", "Enter username")
        return

    random_part = ''.join(random.choice(string.ascii_letters + string.digits + "!@#$%") for _ in range(4))
    password = username + random_part

    password_var.set(password)
    check_strength(password)

def check_strength(password):
    strength = "Weak ❌"
    if len(password) >= 8:
        strength = "Medium ⚠️"
    if len(password) >= 12 and any(c.isdigit() for c in password) and any(c in "!@#$%^&*"):
        strength = "Strong ✅"
    strength_var.set(strength)

def copy_password():
    root.clipboard_clear()
    root.clipboard_append(password_var.get())
    messagebox.showinfo("Copied", "Password copied!")

root = tk.Tk()
root.title("Username Password Generator")
root.geometry("400x300")

tk.Label(root, text="Enter Username").pack()
username_entry = tk.Entry(root)
username_entry.pack()

tk.Button(root, text="Generate Password", command=generate_password).pack(pady=10)

password_var = tk.StringVar()
tk.Entry(root, textvariable=password_var, width=30).pack()

strength_var = tk.StringVar()
tk.Label(root, textvariable=strength_var).pack(pady=5)

tk.Button(root, text="Copy 📋", command=copy_password).pack(pady=10)

root.mainloop()
