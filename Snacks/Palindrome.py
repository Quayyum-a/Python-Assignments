def is_palindrome(s):
    s = s.lower()
    reversed_str = s[::-1]
    return s == reversed_str

if __name__ == "__main__":
    input_str = input("Enter any word to check: ")
    if is_palindrome(input_str):
        print(f"\"{input_str}\" is a palindrome.")
    else:
        print(f"\"{input_str}\" is not a palindrome.")
