number = int(input("Enter a number to calculate its factorial: "))

if number < 0:    
	print("Factorial is not defined for negative numbers.")
else:    
	result = 1   
	while number > 1:        
		result *= number        
		number -= 1    
    
	print(f"The factorial of the given number is {result}.")
