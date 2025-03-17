import random
number = random.randint(1,10)
print(number)

found = 0

x = input("Guess the number: ")
while found == 0:
       if int(x) == number: 
           found = 1
       else:
           x = input("Enter number: ")

print("Congratulations!")
