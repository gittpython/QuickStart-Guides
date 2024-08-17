# Define a new class
class Customer:
    # Define the init methind, using name and city as arguments
    def __init__ (self, name, city):
        self.name = name
        self.city = city
        
# Create three objects based on the Customer classs
# The name and city as passed to __init__
c1 = Customer("Sarah", "Alanta")
c2 = Customer("Robert", "Florence")
c3 = Customer("Thomas", "Denver")

