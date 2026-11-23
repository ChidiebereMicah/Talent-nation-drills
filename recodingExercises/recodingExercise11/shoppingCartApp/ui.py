import tkinter as tk
from tkinter import messagebox
import shoppingCart as sh

def on_add_item():
    try:
        cart = cart_entry.get()
        name = name_entry.get()
        price = float(price_entry.get())
        qty = int(qty_entry.get())
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter correct cart name, item name, price and quantity.")
        return
    result_label.config(text = f"Cart status: {sh.add_item(cart, name, price, qty)} has been added to your cart")

def on_remove_item():
    try:
        cart = (cart_entry.get())
        name = (name_entry.get())
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter correct cart name, item name, price and quantity.")
        return
    removed_item = sh.remove_item(cart, name)
    if removed_item is None:
        result_label.config(text = f"{name} + has not been added to cart")
    else:
        result_label.config(text = f"Cart status: {name} has been removed from cart")

def on_view_cart():
    try:
        cart = cart_entry.get()
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter correct cart name")
        return
    result_label.config(text = f"Cart status: {sh.add_item(cart)} has been added to your cart")


def on_clear():
    cart_entry.delete(0, tk.END)
    name_entry.delete(0, tk.END)
    price_entry.delete(0, tk.END)
    qty_entry.delete(0, tk.END)
    result_label.config(text="Cart status: ")

root = tk.Tk()
root.title("SHoppING CarT")
root.geometry("960x720")

tk.Label(root, text="Cart name:").pack()
cart_entry = tk.Entry(root)
cart_entry.pack()

tk.Label(root, text="Item name:").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Price:").pack()
price_entry = tk.Entry(root)
price_entry.pack()

tk.Label(root, text="QTY:").pack()
qty_entry = tk.Entry(root)
qty_entry.pack()

#Buttons
tk.Button(root, text="Add item", command=on_add_item).pack(pady=5)
tk.Button(root, text="Remove item", command=on_remove_item).pack(pady=5)
tk.Button(root, text="View cart", command=on_view_cart).pack(pady=5)
tk.Button(root, text="Clear", command=on_clear).pack()

result_label = tk.Label(root, text="Cart status: ")
result_label.pack(pady=10)

root.mainloop()