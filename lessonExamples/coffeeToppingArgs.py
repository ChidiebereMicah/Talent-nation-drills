"""
Write a function that accepts any arbitrary number of positional coffee toppings 
(like chocolate, sprinkles, and whipped cream) 
using *args without explicitly declaring each topping name as a separate parameter.
"""

def coffee_topping(*args):
    return f"The following topping flavors should accompany your new coffee machine: {arg for arg in args}"