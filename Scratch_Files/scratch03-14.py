# the planets
# Enumaerate

planets = ("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune")

# Display the plant and its number
for index, value in enumerate(planets):
    print("Plnet " + str(index) + ": " + value)
print("===========X==============")
print("Abs for the the adjusted\n")
# Display the plant and its real number
for index, value in enumerate(planets):
    print("Plnet " + str(index + 1) + ": " + value)