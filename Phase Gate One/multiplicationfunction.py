def get_multiplication(number1, number2):
    total = 0
    for _ in range (0, number2):
        total += number1
    return round(total, 1)
        
def get_invalid(number3, number4):
    return 'invalid input' if type (number3) == str or type (number4) == str else number4