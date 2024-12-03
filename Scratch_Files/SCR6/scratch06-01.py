# Defing the World class
# Page 114

class World:
    # Define our greeting
    greeting = "Hello, World"
    
    # Run this whenever the opbject is created
    def __init__ (self):
        # Print the greeting
        print(self.greeting)
        
# Use the class World to create a world object named w
w = World()
