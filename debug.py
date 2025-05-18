from customer import Customer
from coffee import Coffee
from order import Order

c1 = Customer("Roddy")
c2 = Customer("Joan")
c3 = Customer("Sarah")

coffee1 = Coffee("Latte")
coffee2 = Coffee("Espresso")

c1.create_order(coffee1, 3.5)
c1.create_order(coffee2, 4.0)
c2.create_order(coffee1, 6.5)
c2.create_order(coffee1, 7.0)

print("C1 Coffees:", [c.name for c in c1.coffees()])
print("Coffee1 num_orders:", coffee1.num_orders())
print("Coffee1 avg price:", coffee1.average_price())
print("Aficionado:", Customer.most_aficionado(coffee1).name)
