#ClydeBank Coffee Shop Simulator 4000
#Copyright 2024 (c) ClydeBank Media, All Rights Reserved.
# Current day number
day = 1
#Sales list of disctionaries
#sales = [
    # {
    #     "day": 1.
    #     "coffee_inv": 100,
    #     "advertising": "10",
    #     "temp": 68,
    #     "cups_sold": 26
    # },
   # {
    #     "day": 2.
    #     "coffee_inv": 84,
    #     "advertising": "15",
    #     "temp": 72,
    #     "cups_sold": 20
    # },
   # {
    #     "day": 3.
    #     "coffee_inv": 64,
    #     "advertising": "5",
    #     "temp": 78,
    #     "cups_sold": 10
    # },
#]

# Create an empty sales list
sales=[]

#print Welcome message
print("ClydeBank Coffee Shop Simulator 4000, Version 1.00")
print("Copyright 2024 (c) ClydeBank Media, All Rights Reserved.\n")
print("Let's collect some information before we start the game.\n")

# Get name and shop name
name = input("What is your name? ")
shop_name = input("What do you want to name your coffee shop? ")

print("\nThanks, " + name + ". Let’s set some initial pricing.\n")

# Get initial price of a cup of coffee
cup_price = input("What do you wnat to charge per cup of coffee? ")

#Display what we have
print("\nGreat. Here's what we've collected do far.\n")
print("Your name is " + name + "and you're opening " + shop_name + "!")
print("Your first cup of coffee will sell for $" + str(cup_price) + " Wow !!!.\n")