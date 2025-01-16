number1 = 1
number2 = 1

print("Multiples of 4:")
for _ in range(5):  
    number1 *= 4
    number1 += number1
    print(number1)

print("\nMultiples of 8:")
for _ in range(5):  
    number2 *= 8
    print(number2)