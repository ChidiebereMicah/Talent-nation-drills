
class Cart():

    def __init__(self, name, price, qty):
        self.cart = [{"name": name, "price": price, "qty": qty}]
        
    def add_cart():
        pass

    def view_all_carts():
        pass

    def add_item(self, name, price, qty):
        for item in self.cart[1::]:
            if name in item:
                item[qty] += 1
                break
            else:
                cart.append({"name": name, "price": price, "qty": qty})
                break
        return name

    def remove_item(cart, name):
        for idx, item in enumerate(cart):
            if item[name] == name:
                cart.pop(idx)
                return name
        return None

    def view_cart(cart):
        return [item for item in cart]

    def cart_total(cart):
        return sum(item["price"] for item in cart)

    def apply_discount(total, percent):
        return round(total*percent/100, 2)
    