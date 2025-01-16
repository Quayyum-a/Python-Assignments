binary = int(input("Enter a binary number: "))

decimal = 0
power = 1

while binary > 0:
    digit = binary % 10  
    decimal += digit * power
    binary //= 10  
    power *= 2 

print(f"The decimal equivalent is: {decimal}")
