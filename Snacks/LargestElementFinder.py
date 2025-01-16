def find_largest(array):
    largest = array[0]
    for count in array:
        if count > largest:
            largest = count
    return largest

if __name__ == "__main__":
    entry = int(input("Enter the number of elements: "))
    
    numbers = []
    
    print(f"Enter {entry} numbers:")
    for count in range(entry):
        number = int(input(f"Number {count + 1}: "))
        numbers.append(number)
    
    largest = find_largest(numbers)
    
    print(f"The largest number is: {largest}")
