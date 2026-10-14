class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price  # Вызывается setter для проверки цены

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, value: float):
        if value < 0:
            self._price = 0.0
        else:
            self._price = float(value)


# Пример использования:
product = Product("Book", 10)
print(product.price)  
product.price = -5
print(product.price)  
