#Hayden Cowart, Sam Rolfson, Joshua Thatcher, Cristian Cruz, Garrett Brand
#This is the work for the Group Hamburger Door Dash Assignment
import random
from queue import Queue

# Creates an Order with a random number of burgers ordered
class Order:
    def __init__(self):
        self.burger_count = self.randomBurgers()
        
    def randomBurgers(self):
        return random.randint(1, 20)

# Creates a random Person
class Person:
    def __init__(self):
        self.customer_name = self.randomName()
        
    def randomName(self):
        asCustomers = ["Jefe", "El Guapo", "Lucky Day", "Ned Nederlander", "Dusty Bottoms", "Harry Flugleman", "Carmen", "Invisible Swordsman", "Singing Bush"]
        return random.choice(asCustomers)

# Creates a Customer that uses the Person class and Order class
class Customer(Person):
    def __init__(self):
        super().__init__() 
        self.order = Order()

# Creates a queue to place Customers in
customer_queue = Queue()
customer_dict = {}

# Creates and updates Customer's orders 100 times
for _ in range(100):
    customer = Customer()
    customer_queue.put(customer)
    if customer.customer_name in customer_dict:
        customer_dict[customer.customer_name] += customer.order.burger_count
    else:
        customer_dict[customer.customer_name] = customer.order.burger_count

# Sorts the Customer Dictionary based on Burger Count
sorted_customers = sorted(customer_dict.items(), key=lambda x: x[1], reverse=True)

# Creates an even length to seperate the Customer and Burger Count
max_name_length = max(len(customer_name) for customer_name, _ in sorted_customers)
ljust_value = max_name_length + 2

# Prints out Customers and Burger Counts
for customer_name, burger_count in sorted_customers:
    formatted_name = customer_name.ljust(ljust_value)
    print(f"Customer: {formatted_name} - Total Burgers Ordered: {burger_count}")


