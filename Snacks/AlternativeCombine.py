def alternate_combine(list1, list2):
    result = []
    max_length = max(len(list1), len(list2))

    for count in range(max_length):
        if count < len(list1):
            result.append(list1[count])
        if count < len(list2):
            result.append(list2[count])

    return result

if __name__ == "__main__":
    list1 = ['a', 'b', 'c', 'd']
    list2 = ["welcome", 4, 22]

    print("Alternating List:", alternate_combine(list1, list2))
