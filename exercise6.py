number = int(input("Enter a number to caculate its factorial: "))


if number < 0:
    print("Factorial is not defined for negative numbers.")
else:
    result = 1
    for i in range(1, number + 1):
        result *= i
   
    print(f"The factorial of the given number is {result}.")
