# THe hedader info
# 
from random import seed
from random import randint
number = randint(1, 10)

print("This is a ramdom number game")
print("Simple to follow along")
usrInput = input("Pick  number between 1 and 10: ")
 #verify the number
if usrInput >= 11:
     print("you idiot, cant you read? Try again\n")
elif usrInput <= 0:
     print("You are trying me...")
print("So you selected " + usrInput)
print("it is not")

     
     