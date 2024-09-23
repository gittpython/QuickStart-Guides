
# Fizzbuzz

count = 1

while(count <= 100):
	if (count % 3 ==0) and (count % 5 ==0):
		print(f"{count}. FizzBuzz")
	elif (count % 3 == 0):
		print(f'{count}.Fizz')
	elif (count % 5 == 0):
		print(f'{count}.Buzz')
	else:
		print(f"{count}.")
	count+=1
