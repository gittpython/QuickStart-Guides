# Define a new class Page 124
class World:
    # Define the init methind, using name and city as arguments
    def __init__ (self):
        print("I am alive !")
    
    def __del__(self):
        print("I'm gone!")
        # Run codeupon entering scope of with statement 
    
    
earth = World()
del(earth)
        