def get_digits(number):
    digits = []
    while number > 0:
        digits.insert(0, number % 10)
        number //= 10
    return digits

if __name__ == "__main__":
    number = 2342
    print("Digits:", get_digits(number))
