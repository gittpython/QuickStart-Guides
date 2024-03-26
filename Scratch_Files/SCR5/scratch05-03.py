# Define function full_name
def full_name(first, middle,  last, display):
    name = first + " " + middle + " " + last
    if display:
        print(name)
    return name

# Use our new creted function
full_name("Robert", "W", "Oliver", True)
complete_name = full_name("Robert", "W", "Oliver", False)
print(complete_name)


x = 5

def double(x):
    x = x * 2
double(x)
print(x)

x = 5

def double(n):
    return n * 2
x = double(x)
print(x)