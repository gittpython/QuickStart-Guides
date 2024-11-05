# Define a new class Page 124
# Convert kilometers to miles
class Converter:
    # Define the init methind
    def __init__ (self, km):
        self.km = km
    
    def to_miles(self):
        return self.km / 1.609

# Convert 2 kilometers to miles
distance1 = Converter(3)
print(distance1.to_miles())
 