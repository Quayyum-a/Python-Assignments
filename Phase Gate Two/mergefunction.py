def merge_list(number1:list, number2:list)->list:
    merged_list = []
    length = max(len(number1), len(number2))
    
    for count in range(length):
        if count < len(number1):
            merged_list.append(number1[count])
        if count < len(number2):
            merged_list.append(number2[count])
            
    return merged_list