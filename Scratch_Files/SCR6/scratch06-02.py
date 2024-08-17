# Defing a new class

class Customer:
    def __init__ (self, name, city):
        self.name = name
        self.city = city
        
    def greet(self):
        print("Hello, " + self.name + "!")
        
# Create three opbects based on the Customer classs
c1 = Customer("Sarah", "Alanta")
c2 = Customer("Robert", "Florence")
c3 = Customer("Thomas", "Denver")

# Add the custtomer objects to the list
customers = [c1, c2, c3]


# Iterate through list, greet, then display information
for c in customers:
    c.greet()
    print(c.name + " lives in "+ c.city +".")