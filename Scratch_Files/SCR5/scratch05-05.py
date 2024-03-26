# Define function full_name
def full_name(first = "First", middle = "Middel", last = "Last", display = False):
    name = first + " " + middle + " " + last
    if display:
        print(name)
    return name

def full_name(first, middle, last, display = False):
    