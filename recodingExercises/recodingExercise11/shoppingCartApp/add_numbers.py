import tkinter as tk
from tkinter import messagebox

# ---------- LOGIC (no tkinter in here) ----------
def add_numbers(a, b):
    return a + b

# ---------- WINDOW CODE ----------
def on_add():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter numbers only.")
        return
    result_label.config(text="Result: " + str(add_numbers(a, b)))

def on_clear():
    entry_a.delete(0, tk.END)
    entry_b.delete(0, tk.END)
    result_label.config(text="Result: ")

root = tk.Tk()
root.title("My First App")
root.geometry("320x240")

tk.Label(root, text="First number:").pack()
entry_a = tk.Entry(root)
entry_a.pack()

tk.Label(root, text="Second number:").pack()
entry_b = tk.Entry(root)
entry_b.pack()

tk.Button(root, text="Add", command=on_add).pack(pady=5)
tk.Button(root, text="Clear", command=on_clear).pack()

result_label = tk.Label(root, text="Result: ")
result_label.pack(pady=10)

root.mainloop()