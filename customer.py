class Customer:
    def __init__(self, name):
        self._name = None
        self.name = name 

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 15:
            self._name = value
        else:
            raise ValueError("Name must be a string between 1 and 15 characters")


from order import Order

def orders(self):
    return [order for order in Order._all if order.customer == self]

def coffees(self):
    return list({order.coffee for order in self.orders()})

def create_order(self, coffee, price):
    return Order(self, coffee, price)

Customer.orders = orders
Customer.coffees = coffees
Customer.create_order = create_order
