try:
    num1 = int(input("Enter first number: "))
except ValueError:
    print("Invalid input, Please retry and enter an integer.")
    exit()
try:
    num2 = int(input("Enter second number: "))
except ValueError:
    print("Invalid input, Please retry and enter an integer.")
    exit()
try:
    num3 = int(input("Enter third number: "))
except ValueError:
    print("Invalid input, Please retry and enter an integer.")
    exit()

ascending_numbers = sorted([num1, num2, num3])
print(ascending_numbers)
