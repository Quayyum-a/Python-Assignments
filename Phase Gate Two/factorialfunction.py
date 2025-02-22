def get_factorial(number:int)-> int:
    result = 1
    for count in range(1, number + 1):
        result *= count
    return result


