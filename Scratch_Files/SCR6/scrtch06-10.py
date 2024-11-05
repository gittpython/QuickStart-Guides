# Define a new class Page 124
# Convert kilometers to miles
class Distance:
    # Define the init methind
    def __init__ (self, km):
        self._km = km
    
    @property
    def km(self):
        return self._km
        
    @property
    def miles(self):
        return self._km / 1.609

# Convert 2 kilometers to miles
distance2 = Distance(3)
print(str(distance2.km))
print(str(distance2.miles))
 