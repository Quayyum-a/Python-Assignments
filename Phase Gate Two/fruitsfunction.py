def get_fruits(fruits:list)->list:
    upper_fruits =[]
    for count in fruits:
        upper_fruits.append(count.upper())
    return upper_fruits
    
    
def get_square(numbers:list)->list:
    square_numbers = []
    count = 0
    while count <= len(numbers):
        count *= 2
    return count