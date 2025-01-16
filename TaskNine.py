number1 = 1
number2 = 1
number = 0


for _ in range(5):  
    number1 *= 4
    number += number1


for _ in range(5):  
    number2 *= 8
    number += number2
    result = number * number
print(result)