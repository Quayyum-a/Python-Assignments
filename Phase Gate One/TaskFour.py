try:
    entry = int(input("Enter a value from 0 - 1000: "))
except ValueError:
    print("Invalid input. Please enter an integer.")
    exit()
sum_of_digits = 0

while entry > 0:
    digit = entry % 10 
    sum_of_digits += digit 
    entry //= 10  

print("Sum of the digits:", sum_of_digits)
