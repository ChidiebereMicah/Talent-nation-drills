"""
ReceiptFormatter

Instructions
Implement receipt_formatter(name, quantity, price). 
Calculate subtotal as quantity multiplied by price. 
Calculate tax as 7.5 percent of subtotal. 
Calculate total as subtotal plus tax. 
Return a four-line report with labels Customer, Subtotal, Tax, and Total. 
Round subtotal, tax, and total to 2 decimal places.
"""

def receipt_formatter(name, quantity, price):
    customer = name
    quantity = float(quantity)
    price = float(price)
    subtotal = round(quantity*price,2)
    tax = round(0.075*subtotal,2)
    total = round(subtotal + tax, 2)
    return f"Customer: {customer}\nSubtotal: {subtotal}\nTax: {tax}\nTotal: {total}"

