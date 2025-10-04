#exercise 2 OOP
# The first step was to define product class
class product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_value(self):
        self.total_value = self.price *self.quantity
        return self.total_value
    def display_product_info(self):
        return f"Product:{self.name} Price:{self.price} Quantity:{self.quantity} Total_value:{self.total_value()}"
    
product1 = product("phone", 1000, 3 )
product2 = product('apple', 20, 5)
product3 = product("Shoe", 50, 3)

print(product1.display_product_info())
print(product2.display_product_info())
print(product3.display_product_info())