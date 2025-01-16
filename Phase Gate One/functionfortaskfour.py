def get_digit(number):
    return 'invalid data' if type (number) == str or number < 0 else number % 10
    
def remove_digit(number):
    return number // 10