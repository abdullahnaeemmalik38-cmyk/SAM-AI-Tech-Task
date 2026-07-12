
import customtkinter as ctk
from tkinter import messagebox
import datetime

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

def caesar_cipher(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char

    return result

def get_selected_text():
    if source_var.get() == "input":
        return input_box.get("1.0", "end").strip()
    else:
        return output_box.get("1.0", "end").strip()


def encrypt():
    text = get_selected_text()

    if not text:
        messagebox.showwarning(
            "Warning",
            f"No text found in {source_var.get().capitalize()} Box."
        )
        return

    try:
        shift = int(shift_entry.get())
    except ValueError:
        messagebox.showerror(
            "Error",
            "Shift must be a number."
        )
        return

    result = caesar_cipher(text, shift)

    output_box.delete("1.0", "end")
    output_box.insert("end", result)

    add_history(
        "ENCRYPT",
        source_var.get().upper(),
        text,
        result
    )


def decrypt():
    text = get_selected_text()

    if not text:
        messagebox.showwarning(
            "Warning",
            f"No text found in {source_var.get().capitalize()} Box."
        )
        return

    try:
        shift = int(shift_entry.get())
    except ValueError:
        messagebox.showerror(
            "Error",
            "Shift must be a number."
        )
        return

    result = caesar_cipher(text, -shift)

    output_box.delete("1.0", "end")
    output_box.insert("end", result)

    add_history(
        "DECRYPT",
        source_var.get().upper(),
        text,
        result
    )


def clear_all():
    input_box.delete("1.0", "end")
    output_box.delete("1.0", "end")
    shift_entry.delete(0, "end")


def clear_history():
    history_box.delete("1.0", "end")


def copy_result():
    result = output_box.get("1.0", "end").strip()

    if result:
        app.clipboard_clear()
        app.clipboard_append(result)
        messagebox.showinfo(
            "Success",
            "Result copied to clipboard."
        )


def add_history(operation, source, original, result):
    time = datetime.datetime.now().strftime("%H:%M:%S")

    entry = (
        f"[{time}] {operation}\n"
        f"Source: {source}\n"
        f"Input: {original}\n"
        f"Output: {result}\n"
        f"{'-' * 40}\n"
    )

    history_box.insert("end", entry)

    with open("history.txt", "a", encoding="utf-8") as file:
        file.write(entry + "\n")

app = ctk.CTk()
app.title("Caesar Cipher Encryption & Decryption Tool")
app.geometry("1200x700")

source_var = ctk.StringVar(value="input")

title = ctk.CTkLabel(
    app,
    text=" Caesar Cipher Encryption & Decryption",
    font=("Segoe UI", 28, "bold")
)
title.pack(pady=20)

main_frame = ctk.CTkFrame(app)
main_frame.pack(fill="both", expand=True, padx=20, pady=10)

left_frame = ctk.CTkFrame(main_frame)
left_frame.pack(
    side="left",
    fill="both",
    expand=True,
    padx=10,
    pady=10
)

ctk.CTkLabel(
    left_frame,
    text="Input Message",
    font=("Segoe UI", 18, "bold")
).pack(pady=(15, 10))

input_box = ctk.CTkTextbox(
    left_frame,
    height=150
)
input_box.pack(
    fill="x",
    padx=15
)


ctk.CTkLabel(
    left_frame,
    text="Shift Value",
    font=("Segoe UI", 18, "bold")
).pack(pady=(15, 10))

shift_entry = ctk.CTkEntry(
    left_frame,
    width=200,
    height=35
)
shift_entry.pack()


source_frame = ctk.CTkFrame(left_frame)
source_frame.pack(pady=15)

ctk.CTkLabel(
    source_frame,
    text="Select Source Box",
    font=("Segoe UI", 16, "bold")
).pack(pady=5)

input_radio = ctk.CTkRadioButton(
    source_frame,
    text="Input Box",
    variable=source_var,
    value="input"
)
input_radio.pack(side="left", padx=15, pady=10)

output_radio = ctk.CTkRadioButton(
    source_frame,
    text="Output Box",
    variable=source_var,
    value="output"
)
output_radio.pack(side="left", padx=15, pady=10)


button_frame = ctk.CTkFrame(left_frame)
button_frame.pack(pady=20)

encrypt_btn = ctk.CTkButton(
    button_frame,
    text="Encrypt",
    command=encrypt,
    width=140,
    height=40
)
encrypt_btn.grid(row=0, column=0, padx=10, pady=10)

decrypt_btn = ctk.CTkButton(
    button_frame,
    text="Decrypt",
    command=decrypt,
    width=140,
    height=40
)
decrypt_btn.grid(row=0, column=1, padx=10, pady=10)

copy_btn = ctk.CTkButton(
    button_frame,
    text="Copy Result",
    command=copy_result,
    width=140,
    height=40
)
copy_btn.grid(row=1, column=0, padx=10, pady=10)

clear_btn = ctk.CTkButton(
    button_frame,
    text="Clear All",
    command=clear_all,
    width=140,
    height=40
)
clear_btn.grid(row=1, column=1, padx=10, pady=10)

ctk.CTkLabel(
    left_frame,
    text="Output Message",
    font=("Segoe UI", 18, "bold")
).pack(pady=(10, 10))

output_box = ctk.CTkTextbox(
    left_frame,
    height=150
)
output_box.pack(
    fill="x",
    padx=15,
    pady=(0, 15)
)


right_frame = ctk.CTkFrame(
    main_frame,
    width=350
)
right_frame.pack(
    side="right",
    fill="both",
    padx=10,
    pady=10
)

ctk.CTkLabel(
    right_frame,
    text="History",
    font=("Segoe UI", 22, "bold")
).pack(pady=15)

history_box = ctk.CTkTextbox(
    right_frame
)
history_box.pack(
    fill="both",
    expand=True,
    padx=10,
    pady=10
)

clear_history_btn = ctk.CTkButton(
    right_frame,
    text="Clear History",
    command=clear_history
)
clear_history_btn.pack(
    pady=10
)

app.mainloop()

