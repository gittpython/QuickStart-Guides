# THe hedader info
# 
from random import seed
from random import randint
number = randint(1, 9)

print("This is a ramdom number game")

print("Simple to follow along, pick a number: ")

upick = input("What is your pic")
while upick == number:
     print("Good Guess")
if int(upick != number):
     print("The number is" + " " + str(number))
     if int(upick) == number:
          print("YOU WON")
     elif int(upick) < number:
          print("lower")
     elif int(upick) > number:
          print("higher")
     else:
          upick = False

     print("helloooooo")
     # upick = input("guess again: ")