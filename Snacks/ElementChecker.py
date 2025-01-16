def element_in_list(lst, element):
    for item in lst:
        if item == element:
            return True
    return False

if __name__ == "__main__":
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    target = int(input("Please enter the element you want from 1 - 10: "))
    
    result = element_in_list(lst, target)
    print(f"Is element {target} in the list? {result}")
