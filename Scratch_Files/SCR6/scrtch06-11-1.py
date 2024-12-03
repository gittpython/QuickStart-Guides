# Define a new class Page 127
# Convert kilometers to miles
class Distance:
    # Define the init methind
    def __init__ (self, inches):
        self._inches = inches
    
    @property
    def inches(self):
        return self._inchess
        
    @inches.setter
    def inches(self, value):
        self._inches= value
        
    @property
    def centimeters(self):
        return self._inches * 2.54
    
    @centimeters.setter
    def cnetimeters(self, value):
        self._inches = value * 2.54
        

# Convert 2 centemeters to inches
distance2 = Distance(4)
print("4 inches is "+ str(distance2.cnetimeters) + " centemeters.")
distance2.cnetimeters = 4
print(str(distance2.centimeters) + " centimeters is " + str(distance2) + " inches.")
print(str(distance2.centimeters))
print(str(distance2.centimeters))
 