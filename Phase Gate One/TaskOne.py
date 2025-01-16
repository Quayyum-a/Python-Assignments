import random

num1 = random.randrange(0, 100)
num2 = random.randrange(0, 100)

print(num1, " + ", num2)

sum_result = num1 + num2

try: 
    result = int(input("Enter the sum of both digits: "))
except ValueError:
    print("Invalid input, Please retry and enter an integer.")
    exit()
else:
    if result == sum_result:
        print("True")
    else:
        print("False")
