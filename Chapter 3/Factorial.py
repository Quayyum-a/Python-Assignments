entry = int(input('Enter a number to check its factorial: '))

if entry < 0:
    print("Factorial is not defined for negative numbers.")
elif entry == 0 or entry == 1:
    print(f"The factorial of {entry} is 1.")
else:
    factorial = 1
    for integer in range(1, entry + 1):  
        factorial *= integer 
    print(f"The factorial of {entry} is {factorial}.")
