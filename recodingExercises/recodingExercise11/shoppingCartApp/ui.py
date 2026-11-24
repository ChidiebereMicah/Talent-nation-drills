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
    sh.add_item(sh.cart, name, price, qty)
    result_label.config(text = f"Cart status: {name} has been added to your cart")

def on_remove_item():
    try:
        cart = (cart_entry.get())
        name = (name_entry.get())
    except ValueError, KeyError:
        messagebox.showerror("Invalid input", "Please enter correct cart name, item name, price and quantity.")
        return
    removed_item = sh.remove_item(sh.cart, name)
    if removed_item is None:
        result_label.config(text = f"{name} + has not been added to cart")
    else:
        result_label.config(text = f"Cart status: {name} has been removed from cart")

def on_view_cart():
    result_label.config(text = f"Your cart contains: {sh.view_cart(sh.cart)}")

def on_cart_total():
    total = sh.cart_total(sh.cart)
    result_label.config(text = f"Total price of cart: {sh.cart_total(sh.cart)}")

def on_apply_discount():
    try:
        discount = float(discount_entry.get())
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter correct discount percentage.")
        return
    discounted_price = sh.apply_discount(sh.cart_total(sh.cart), discount)
    result_label.config(text = f"Discounted price of cart: {discounted_price}")    

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

tk.Label(root, text="Discount percentage:").pack()
discount_entry = tk.Entry(root)
discount_entry.pack()

#Buttons
tk.Button(root, text="Add item", command=on_add_item).pack(pady=5)
tk.Button(root, text="Remove item", command=on_remove_item).pack(pady=5)
tk.Button(root, text="View cart", command=on_view_cart).pack(pady=5)
tk.Button(root, text="Calculate total", command=on_cart_total).pack(pady=5)
tk.Button(root, text="Apply discount", command=on_apply_discount).pack(pady=5)
tk.Button(root, text="Clear", command=on_clear).pack()

result_label = tk.Label(root, text="Cart status: ")
result_label.pack(pady=10)

root.mainloop()