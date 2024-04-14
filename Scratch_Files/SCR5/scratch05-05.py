# Define function full_name
def full_name(first = "First", middle = "Middel", last = "Last", display = False):
    name = first + " " + middle + " " + last
    if display:
        print(name)
    return name

# this works because the last variable provides a default value
def full_name(first, middle, last, display = False):
    name = first + " " + middle + " " + last
    if display:
        print(name)
    return name

# This works because the last two veriables provide a default value
def full_name(first, middle, last = "Last", display = False):
    name = first + " " + middle + " " + last
    if display:
        print(name)
    return name

# this dont work, because a required variable comes after one with a defaukt value
#def full_name(first = "First", middle, last, display = False):
#    name = first + " " + middle + " " + last
#    if display:
#        print(name)
#    return name

def full_name(first , middle, last, display = False):
    name = first + " " + middle + " " + last
    if display:
        print(name + " Naa")
print("Output: ")       
print(full_name(first = "Robert", middle = "W", last = "Oliver"))
print("Mixed order: ")
print(full_name(last = "Oliver", first = "Robert", middle = "W"))
print("Different")
print(full_name(last = "Oliver", first = "Robert", middle = "W", display = True))