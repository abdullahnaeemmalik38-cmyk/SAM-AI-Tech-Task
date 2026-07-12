import tkinter as tk
import re
def check_password():
    password = entry_password.get()
    score = 0
    if len(password) >= 8:
        score += 1
    if re.search(r"[A-Z]", password):
        score += 1
    if re.search(r"[a-z]", password):
        score += 1
    if re.search(r"[0-9]", password):
        score += 1
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    if score <= 2:
        result_label.config(text="Password Strength: Weak", fg="red")
    elif score <= 4:
        result_label.config(text="Password Strength: Medium", fg="orange")
    else:
        result_label.config(text="Password Strength: Strong", fg="green")

def toggle_password():
    if entry_password.cget("show") == "*":
        entry_password.config(show="")
        eye_button.config(text="🙈 Hide")
    else:
        entry_password.config(show="*")
        eye_button.config(text="👁 Show")

root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("450x250")
root.resizable(False, False)
title = tk.Label(root, text="Password Strength Checker",
                 font=("Arial", 16, "bold"))
title.pack(pady=10)
label = tk.Label(root, text="Enter Password:")
label.pack()
frame = tk.Frame(root)
frame.pack(pady=5)
entry_password = tk.Entry(frame, width=30, show="*", font=("Arial", 11))
entry_password.pack(side=tk.LEFT, padx=5)
eye_button = tk.Button(frame, text="👁 Show", command=toggle_password)
eye_button.pack(side=tk.LEFT)

check_button = tk.Button(root,
                         text="Check Strength",
                         command=check_password,
                         bg="blue",
                         fg="white",
                         font=("Arial", 10, "bold"))
check_button.pack(pady=15)

result_label = tk.Label(root,
                        text="",
                        font=("Arial", 12, "bold"))
result_label.pack()
root.mainloop()