def sum_even_numbers(number:list)-> int:
    even_sum = 0
    for count in number:
        if count % 2 == 0:
            even_sum += count
            
    return even_sum
        