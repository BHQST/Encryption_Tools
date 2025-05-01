#!/usr/bin/env python3

import tkinter as tk
from tkinter import ttk, messagebox
from atbash_core import GreekAtbashCipher

cipher = GreekAtbashCipher()

def run_cipher():
    text = input_text.get("1.0", tk.END).strip()

    if upper_var.get() == 1:
        case = 'upper'
    elif lower_var.get() == 1:
        case = 'lower'
    else:
        messagebox.showwarning("Case Selection", "Please select either Upper or Lower case.")
        return

    if not text:
        messagebox.showwarning("Input Required", "Please enter some Greek text.")
        return

    normalized_text = cipher.normalize_text(text)
    if not all(c in cipher.gematria or c.isspace() for c in normalized_text):
        messagebox.showwarning("Invalid Input", "Please enter only Greek letters.")
        return

    try:
        shift = rot_var.get()
        if shift > 0:
            result = cipher.rotate(text, shift, case)
        else:
            result = cipher.encrypt(text, case)

        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, f"Encrypted Text:\n{result['encrypted']}\n\n")
        result_text.insert(tk.END, f"Original Gematria: {result['gematria_original']} (Sum: {result['sum_original']})\n")
        result_text.insert(tk.END, f"Encrypted Gematria: {result['gematria_encrypted']} (Sum: {result['sum_encrypted']})\n")
        result_text.yview(tk.END)

    except Exception as e:
        messagebox.showerror("Error", str(e))


def on_right_click(event, widget):
    context_menu = tk.Menu(widget, tearoff=0)
    context_menu.add_command(label="Copy", command=lambda: widget.event_generate("<Control-c>"))
    context_menu.add_command(label="Paste", command=lambda: widget.event_generate("<Control-v>"))
    context_menu.post(event.x_root, event.y_root)

# GUI layout
root = tk.Tk()
root.title("Greek Atbash Cipher")
root.configure(bg="#f0f0f0")

# Configure resizing
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)  # Input
root.grid_rowconfigure(7, weight=1)  # Output

# Label
ttk.Label(root, text="Enter Greek Text:", background="#f0f0f0").grid(row=0, column=0, sticky="w", padx=5, pady=(5, 0))

# Input Text Box with Scrollbar
input_frame = tk.Frame(root, bg="#f0f0f0")
input_frame.grid(row=1, column=0, sticky="nsew", padx=5)

input_frame.grid_columnconfigure(0, weight=1)
input_frame.grid_rowconfigure(0, weight=1)

input_text = tk.Text(input_frame, height=8, width=40, wrap=tk.WORD, bg="#ffffff", fg="#000000", font=("Arial", 12))
input_text.grid(row=0, column=0, sticky="nsew")

input_scroll = tk.Scrollbar(input_frame, orient=tk.VERTICAL, command=input_text.yview)
input_scroll.grid(row=0, column=1, sticky="ns")
input_text.config(yscrollcommand=input_scroll.set)

input_text.bind("<Button-3>", lambda event: on_right_click(event, input_text))

ttk.Label(root, text="Select Output Case:", background="#f0f0f0").grid(row=2, column=0, pady=5)

# Output Case Section
upper_var = tk.IntVar()
lower_var = tk.IntVar()

def toggle_upper():
    if upper_var.get():
        lower_var.set(0)

def toggle_lower():
    if lower_var.get():
        upper_var.set(0)

case_frame = tk.Frame(root, bg="#f0f0f0")
case_frame.grid(row=3, column=0, pady=2)
case_frame.grid_columnconfigure((0, 1), weight=1)

upper_checkbox = ttk.Checkbutton(
    case_frame,
    text="Upper",
    variable=upper_var,
    command=toggle_upper,
    style="Flat.TCheckbutton"
)
upper_checkbox.grid(row=0, column=0, padx=10, sticky="e")

lower_checkbox = ttk.Checkbutton(
    case_frame,
    text="Lower",
    variable=lower_var,
    command=toggle_lower,
    style="Flat.TCheckbutton"
)
lower_checkbox.grid(row=0, column=1, padx=10, sticky="w")

# ROT Shift Selector
rot_var = tk.IntVar(value=0)
rot_frame = tk.Frame(root, bg="#f0f0f0")
rot_frame.grid(row=4, column=0, pady=5)

ttk.Label(rot_frame, text="ROT Shift:", background="#f0f0f0").pack(side="left", padx=5)
rot_spinbox = tk.Spinbox(rot_frame, from_=0, to=23, textvariable=rot_var, width=5, font=("Arial", 10))
rot_spinbox.pack(side="left")

# Encrypt Button
ttk.Button(root, text="Encrypt", command=run_cipher, style="Hover.TButton").grid(row=5, column=0, pady=10)

# Output Label
ttk.Label(root, text="Encrypted Text Output:", background="#f0f0f0").grid(row=6, column=0, sticky="w", padx=5)

# Output Text Box with Scrollbar
output_frame = tk.Frame(root, bg="#f0f0f0")
output_frame.grid(row=7, column=0, sticky="nsew", padx=5, pady=(0, 5))

output_frame.grid_columnconfigure(0, weight=1)
output_frame.grid_rowconfigure(0, weight=1)

result_text = tk.Text(output_frame, height=8, width=40, wrap=tk.WORD, bg="#f0f0f0", fg="#000000", font=("Arial", 12))
result_text.grid(row=0, column=0, sticky="nsew")

scrollbar = tk.Scrollbar(output_frame, orient=tk.VERTICAL, command=result_text.yview)
scrollbar.grid(row=0, column=1, sticky="ns")
result_text.config(yscrollcommand=scrollbar.set)

result_text.bind("<Button-3>", lambda event: on_right_click(event, result_text))

# Output Label
ttk.Label(root, text="Created by Ghost Squad", background="#f0f0f0", font=("Arial", 10)).grid(row=8, column=0, padx=40)

# Button Styling
style = ttk.Style(root)
style.theme_use("clam")  # Ensures theme allows background changes

style.configure("Hover.TButton",
    font=("Arial", 12),
    background="#4CAF50",
    foreground="white",
    padding=10,
    relief="flat"
)

style.map("Hover.TButton",
    background=[('active', '#388E3C')],
    foreground=[('active', 'white')],
    relief=[('active', 'groove')]  # On hover, change border to 'groove'
)

# Custom style for the checkbuttons to match the root background
style.configure("Flat.TCheckbutton",
    background="#f0f0f0",
    relief="flat",
    borderwidth=0
)
style.map("Flat.TCheckbutton",
    background=[("active", "#f0f0f0")],  # Disable hover effect
    foreground=[("active", "black")]
)

# Run App
root.mainloop()
