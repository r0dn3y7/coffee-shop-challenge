# Coffee Shop Python Project ☕️

## Description

This is a simple Python Object-Oriented Programming (OOP) project for managing a coffee shop's customers, coffee types, and orders. It demonstrates OOP principles such as classes, attributes, methods, and basic relationships .

## Project Structure
coffee-shop-challenge/
├── Pipfile
├── debug.py
├── customer.py
├── coffee.py
├── order.py
└── tests/
    ├── customer_test.py
    ├── coffee_test.py
    └── order_test.py



## Features

- Create customers and coffees
- Track orders between customers and coffees
- Calculate average coffee prices
- Use `@property` decorators for data validation

## Technologies

- Python 3
- OOP concepts (Classes, Properties, Relationships)

## How It Works

### Classes

#### `Customer`
- Stores customer names (1–15 characters)
- Returns a customer's orders
- Lists all unique coffees the customer has ordered

#### `Coffee`
- Tracks different coffee types
- Returns all orders for a coffee
- Calculates average price per coffee

#### `Order`
- Connects a `Customer` and a `Coffee` with a price



---

## How to Run

1. Clone the repo:

```bash
git clone github.com/r0dn3y7/coffee-shop-challenge
cd coffee-shop-challenge

```
2. Set up Python environment:
```
pipenv install
pipenv shell

```
3. Run the debug script for manual testing:
```
python debug.py

```

### Example Usage

```python
c1 = Customer("Alice")
coffee1 = Coffee("Latte")
Order(c1, coffee1, 5.50)


