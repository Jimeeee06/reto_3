class MenuItem:
    def __init__(self, name: str, price: float, amount: int, type: str = None):
        self.type = type
        self.name = name
        self.price = {price}
        self.amount = amount
    def total_price(self):
        return self.price * self.amount
    def __str__(self):
        return f"{self.name} - $ {self.price}"

class Beverage(MenuItem):
    def __init__(self, name: str, price: float, amount: int, flavour: str):
        self.type = "Beverage"
        self.flavour = flavour
        super().__init__(name, price, amount)
    def __str__(self):
        return f"{self.type} - {self.name} - {self.flavour} - $ {self.price}"


class MainCourse(MenuItem):
    def __init__(self, name: str, price: float, amount: int, appetizer: str):
        self.appetizer = appetizer
        self.type = "Main Course"
        super().__init__(name, price, amount)
    def __str__(self):
        return f"{self.type} - {self.name} - $ {self.price}"

class Hamburguer(MenuItem):
    def __init__(self, name: str, price: float, amount: int, flavour: str, size: str):
        self.size = size
        self.flavour = flavour
        self.type = "Hamburguer"
        super().__init__(name, price, amount)
    def __str__(self):
        return f"{self.type} - {self.name} - {self.tipo} - $ {self.price}"

class Pizza(MenuItem):
    def __init__(self, name: str, price: float, amount: int, flavour: str, size: str):
        self.size = size
        self.flavour = flavour
        self.type = "Pizza"
        super().__init__(name, price, amount)
    def __str__(self):
        return f"{self.type} - {self.name} - {self.tipo} - $ {self.price}"

class Salad(MenuItem):
    def __init__(self, name: str, price: float, amount: int, flavour: str, size: str):
        self.size = size
        self.flavour = flavour
        self.type = "Salad"
        super().__init__(name, price, amount)
    def __str__(self):
        return f"{self.type} - {self.name} - {self.tipo} - $ {self.price}"

class Pasta(MenuItem):
    def __init__(self, name: str, price: float, amount: int, flavour: str):
        self.flavour = flavour
        self.type = "Pasta"
        super().__init__(name, price, amount)
    def __str__(self):
        return f"{self.type} - {self.name} - {self.tipo} - $ {self.price}"

class VeganFood(MenuItem):
    def __init__(self, name: str, price: float, amount: int, flavour: str):
        self.flavour = flavour
        self.type = "Vegan"
        super().__init__(name, price, amount)
    def __str__(self):
        return f"{self.type} - {self.name} - $ {self.price}"

class SeaFood(MenuItem):
    def __init__(self, name: str, price: float, amount: int, fish_type: str):
        self.fish_type = fish_type
        self.type = "Sea Food"
        super().__init__(name, price, amount)
    def __str__(self):
        return f"{self.type} - {self.name} - $ {self.price}"

class AsianFood(MenuItem):
    def __init__(self, name: str, price: float, amount: int, flavour: str):
        self.flavour = flavour
        self.type = "Asian Food"
        super().__init__(name, price, amount)
    def __str__(self):
        return f"{self.type} - {self.name} - $ {self.price}"

class Dessert(MenuItem):
    def __init__(self, name: str, price: float, amount: int, flavour: str):
        self.flavour = flavour
        self.type = "Dessert"
        super().__init__(name, price, amount)
    def __str__(self):
        return f"{self.type} - {self.name} - $ {self.price}"

class Soup(MenuItem):
    def __init__(self, name: str, price: float, amount: int, flavour: str):
        self.flavour = flavour
        self.type = "Soup"
        super().__init__(name, price, amount)
    def __str__(self):
        return f"{self.type} - {self.name} - $ {self.price}"

class Order:
    def __init__(self, order_number: int):
        self.order_number = order_number
        self.items = []
        self.total_price = 0
    def add_item(self, item: MenuItem):
        self.items.append(item)
    def remove_item(self, item: MenuItem):
        if item in self.items:
            self.items.remove(item)
        else:
            print("Item not found in the order.")
    def total_price(self):
        total = 0
        for item in self.items:
            total += item.price()
        return total
    def is_discounted(self):
        if self.total_price() > 50:
            return True
        else:
            return False
    def apply_discount(self):
        if self.is_discounted():
            discount = self.total_price() * 0.3
            return discount
        else:
            return "No discount available"
    def __str__(self):
        order_details = f"Order Number: {self.order_number}\n"
        order_details += "Items:\n"
        for item in self.items:
            order_details += str(item) + "\n"
        order_details += f"Total Price: {self.total_price()}"
        return order_details
        
