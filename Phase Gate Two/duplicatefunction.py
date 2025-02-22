def get_duplicate(numbers: list) -> bool:
    for count in range(len(numbers)):
        for counter in range(count + 1, len(numbers)):
            if numbers[count] == numbers[counter]:
                return True
    return False
