def print_odd_positions(numbers):
    for count in range(1, len(numbers), 2):
        print(f"The element at odd position {count + 1} is: {numbers[count]}")

if __name__ == "__main__":
    numbers = [20, 30, 40, 50, 60, 70, 80]
    
    print_odd_positions(numbers)
