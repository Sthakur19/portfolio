class Employee:
    def __init__(self, name):
        self.name = name

class Guest:
    def __init__(self, name):
        self.name = name

class Restaurant:
    def __init__(self, name, priceForMenu):
        self.name = name
        self.menu_price = priceForMenu
        self.customers = []
        self.income = 0

    def sit(self, *args):
        for customer in args:
            self.customers.append(customer)
            

    def serve_menu(self):
        # print(len(self.customers))
        for customer in self.customers:
            if type(customer) == Employee:
                price = self.menu_price / 2
            else:
                price = self.priceForMenu
            self.income = self.income + price
            print(f"{customer.name} is eating for {price}")
        self.customers = []

    def __str__(self):
        return f"{self.name} | {len(self.customers)} customers | menu for {self.priceForMenu}$ | income: {self.income}"

john = Employee('John')
jane = Guest('Jane')
restaurant = Restaurant('Galactica', 10)
print(restaurant)
restaurant.sit(john, jane)
print(restaurant)
restaurant.serve_menu() 
print(restaurant) 