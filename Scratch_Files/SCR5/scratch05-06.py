# Define the average funtion
def average(*numbers):
    sum = 0
    for n in numbers:
        # Addn to sum
        # (+= means add n to sum and store in sum)
        sum += n
        print("The sum now is " + str(sum))
    return sum / len(numbers)
print()
# Use yiur newly minted function
print("The average is: " + str(average(10, 40, 80, 74, 16, 42, 12, 6,)) )   
