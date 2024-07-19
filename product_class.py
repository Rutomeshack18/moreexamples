#Exercise 2: Creating a Product Catalog
# Instruction:
# Define a Product class with attributes like name, price, and quantity.
# Implement a method to calculate the total value of products in stock.
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    def total_value(self):
        return self.price * self.quantity

product1 = Product("Soap", 200, 4)
print(f"The total value of {product1.name} is {product1.total_value()}")