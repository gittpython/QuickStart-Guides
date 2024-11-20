#ClydeBank Coffee Shop Simulator 4000
#Copyright 2024 (c) ClydeBank Media, All Rights Reserved.

# CCS-05 PAGE 109
# Impoer items from the random module to generate weather
from random import seed
from random import randint

# Current day number
day = 1

# Starting cash on hand
cash = 100.00

# Coffee on hand (cups)
coffee = 100

#Sales list of disctionaries
#sales = [
    # {
    #     "day": 1.
    #     "coffee_inv": 100,
    #     "advertising": "10",
    #     "temp": 68,
    #     "cups_sold": 16
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


def welcome():
    #print Welcome message
    print("ClydeBank Coffee Shop Simulator 4000, Version 1.00")
    print("Copyright 2024 (c) ClydeBank Media, All Rights Reserved.\n")
    print("Let's collect some information before we start the game.\n")

def prompt(display ="Please inout a string", require=True):
    if require:
        s = False
        while not s:
            s = input(display + " ")
    else:
        s = input(display + " ")
    return s

def daily_stats(cash_on_hand, weather_temp, coffee_inventory):
    print("You have $" + str(cash_on_hand) + " cash on hand and the temperature is" + str(weather_temp) + ".")
    print("You have enough coffee on hand to make " + str(coffee_inventory) + "cups.\n")
    
def convert_to_float(s):
    # inf conversion fails, assign 0 to it
    try:
        f = float(s)
    except ValueError:
        f = 0
    return f
def get_weather():
    # Generate a random temperature between 20 and 90
    # We'll consider seasons later on, but this is good enough for now
    return randint(20, 90)

# Print welcom message
welcome()

# Get name and shop name 
name = prompt("What is your name?", True)
shop_name = prompt("Waht do you want to name your coffee shop?", True)

# We have what we need, so let's get started!
print("\nOk, let's get started. Have fun!")

#The main game loop
running = True
while running:
    # Display the day and add a "fancy" text effect
    print("\n~~~~~~~| Day " + str(day) + " @ " + shop_name + " |~~~~~~~")
    temperature = get_weather()
 
# using the following approach:
# 1. Ste name and shop_name to False
# 2. Use while no name and shop _name to continue to prompt for a non-empty string

name = False
while not name:
    name = input("What is your name? ")

shop_name = False
while not shop_name:
    shop_name = input("What do you want to name your coffee shop? ")

# we hve what we need, so let's get started
print("\nOK, let's get started. Have fun")

# The main game loop
running = True
while running:
    # Display the day and add a "fancy" text effect
    print("\n------| Day " + str(day) + " @ " + shop_name + " |-----")
    
    # Generate  a random temperature between 20 and 90
    # We will consider seasons later on, but this is good enough for now
    temperature = randint(20, 90)
    
    # Display the cash and weather
    print("You have $" + str(cash) + "cash and it's " + str(temperature) + " degrees.")
    print("You have coffee on hand  to make " + str(coffee) + " cups.\n")
    
    # Get price os a cup of coffee
    cup_price = input("What do you want to charge per cup of coffee? ")
    
    # Get price of a cup of coffee
    print("\n You can buy advertising to help promote sales ")
    advertising = input("How much advertising do you want to buy? (0 for none)? ")
    
    # Convert advertising into float
    # If it fails, assign it to 0
    
    try:
        advertising = float(advertising)
    except ValueError:
        advertising = 0
        
    
    # Deduct advertising from cash on hand
    cash -= advertising
    
    # TODO calculate today's performance
    # TODO Display today's performane
    
    # Before we loop around, add a day
    day += 1
    

    
print("\nThanks, " + name + ". Let’s set some initial pricing.\n")

# Get initial price of a cup of coffee
cup_price = input("What do you wnat to charge per cup of coffee? ")

#Display what we have
print("\nGreat. Here's what we've collected do far.\n")
print("Your name is " + name + "and you're opening " + shop_name + "!")
print("Your first cup of coffee will sell for $" + str(cup_price) + " Wow !!!.\n")