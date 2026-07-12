import tkinter as tk
from tkinter import ttk, messagebox
import random
import string

def generate_password():
    try:
        length = int(length_var.get())
        quantity = int(quantity_var.get())

        if length < 4:
            messagebox.showerror("Error", "Password length must be at least 4.")
            return

        characters = ""

        if letters_var.get():
            characters += string.ascii_letters

        if numbers_var.get():
            characters += string.digits

        if symbols_var.get():
            characters += string.punctuation

        if not characters:
            messagebox.showerror("Error", "Select at least one character type.")
            return

        passwords = []

        for _ in range(quantity):
            while True:
                password = ''.join(random.choice(characters) for _ in range(length))

                # Ensure password is strong
                if (
                    any(c.islower() for c in password)
                    and any(c.isupper() for c in password)
                    and any(c.isdigit() for c in password)
                    and any(c in string.punctuation for c in password)
                ):
                    passwords.append(password)
                    break

        output.delete("1.0", tk.END)
        output.insert(tk.END, "\n".join(passwords))

    except ValueError:
        messagebox.showerror("Error", "Enter valid numbers.")


def copy_password():
    passwords = output.get("1.0", tk.END).strip()

    if passwords:
        root.clipboard_clear()
        root.clipboard_append(passwords)
        messagebox.showinfo("Copied", "Password(s) copied to clipboard!")
    else:
        messagebox.showwarning("Warning", "No password to copy.")

root = tk.Tk()
root.title("Random Password Generator")
root.geometry("500x500")
root.resizable(False, False)

title = tk.Label(
    root,
    text="Strong Password Generator",
    font=("Arial", 18, "bold")
)
title.pack(pady=10)

frame = tk.Frame(root)
frame.pack(pady=10)
tk.Label(frame, text="Password Length:").grid(row=0, column=0, padx=5, pady=5)
length_var = tk.StringVar(value="12")
length_spin = tk.Spinbox(frame, from_=4, to=64, textvariable=length_var, width=10)
length_spin.grid(row=0, column=1)
tk.Label(frame, text="Number of Passwords:").grid(row=1, column=0, padx=5, pady=5)
quantity_var = tk.StringVar(value="1")
quantity_spin = tk.Spinbox(frame, from_=1, to=20, textvariable=quantity_var, width=10)
quantity_spin.grid(row=1, column=1)
letters_var = tk.BooleanVar(value=True)
numbers_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=True)

tk.Checkbutton(root, text="Include Letters", variable=letters_var).pack(anchor="w", padx=50)

tk.Checkbutton(root, text="Include Numbers", variable=numbers_var).pack(anchor="w", padx=50)

tk.Checkbutton(root, text="Include Special Characters", variable=symbols_var).pack(anchor="w", padx=50)
generate_btn = tk.Button(
    root,
    text="Generate Password",
    font=("Arial", 11, "bold"),
    command=generate_password,
    bg="green",
    fg="white"
)
generate_btn.pack(pady=15)

output = tk.Text(root, height=10, width=50, font=("Consolas", 11))
output.pack()

copy_btn = tk.Button(
    root,
    text="Copy Password(s)",
    command=copy_password,
    bg="blue",
    fg="white"
)
copy_btn.pack(pady=10)

root.mainloop()