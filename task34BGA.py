class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @property
    def price(self): return self._price
    @price.setter
    def price(self, v): self._price = max(0.0, float(v))

class Order:
    def __init__(self): 
        self.products = []

    def add_product(self, p): self.products.append(p)
    def remove_product(self, p): p in self.products and self.products.remove(p)

    @property
    def total_price(self): return sum(p.price for p in self.products)

# Тест
book, pen = Product("Book", 10), Product("Pen", 2)
order = Order()
order.add_product(book)
order.add_product(pen)
print(f"Общая стоимость: {order.total_price}")  # 12.0
