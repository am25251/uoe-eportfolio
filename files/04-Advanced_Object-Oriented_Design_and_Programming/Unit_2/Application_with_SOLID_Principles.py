from abc import ABC, abstractmethod

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, product):
        self.items.append(product)

    def total(self):
        return sum(i.price for i in self.items)

class Discount(ABC):
    @abstractmethod
    def apply(self, total):
        pass

class TenPercentDiscount(Discount):
    def apply(self, total):
        return total * 0.90

class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class DebitCard(PaymentMethod):
    def pay(self, amount):
        print(f"Paid €{amount} by Debit Card")

class Checkout:
    def __init__(self, payment_method, discount):
        self.payment_method = payment_method
        self.discount = discount

    def process(self, cart):
        total = cart.total()
        final_total = self.discount.apply(total)
        self.payment_method.pay(final_total)

cart = Cart()
cart.add_item(Product("Laptop Bag", 80))
cart.add_item(Product("Wireless Mouse", 40))

Checkout(DebitCard(), TenPercentDiscount()).process(cart)