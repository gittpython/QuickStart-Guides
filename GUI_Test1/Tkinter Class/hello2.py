import os
import pyttsx3

engine = pyttsx3.init()
# engine.say("Are you telking to me?")

os.system("clear")
engine.say("Please enter your name")

name = input("What is your name? ")

if name == "nigel":
	print("Lower case you're crazy")
	engine.say("crazy")
elif name == "bob":
	print("you're not bob")
else:
	print("hahah")
	engine.say("no match here")

greet = "Hello and welcome to python programming "
print(f"Helloooo " +  name + greet)


engine.say(greet + name)
engine.runAndWait()
