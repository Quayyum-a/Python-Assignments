def print_even_positions(numbers):
    for count in range(2, len(numbers), 2):
        print(f"The element at even position {count + 1} is: {numbers[count]}")

if __name__ == "__main__":
    numbers = [20, 30, 40, 50, 60, 70, 80]
    
    print_even_positions(numbers)
