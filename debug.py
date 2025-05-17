from customer import Customer

c1 = Customer("Roddy")
print(c1.name)

########
from coffee import Coffee

latte = Coffee("Latte")
print(latte.name)


########
from customer import Customer
from coffee import Coffee
from order import Order

c1 = Customer("Alice")
c2 = Customer("Bob")
latte = Coffee("Latte")
mocha = Coffee("Mocha")

order1 = Order(c1, latte, 4.5)
order2 = Order(c2, latte, 5.0)

