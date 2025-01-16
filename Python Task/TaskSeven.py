number1 = 1
number2 = 1
numberAdd1 = 0
numberAdd2 = 0


print("Sum of the multiples of 4:")
for _ in range(5):  
    number1 *= 4
    numberAdd1 += number1
print(numberAdd1)


print("Sum of the multiples of 8:")
for _ in range(5):  
    number2 *= 8
    numberAdd2 += number2
print(numberAdd2)