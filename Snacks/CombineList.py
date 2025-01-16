def combine_three_lists(list1, list2, list3):
    combined_list = []
    combined_list.extend(list1)
    combined_list.extend(list2)
    combined_list.extend(list3)
    return combined_list

if __name__ == "__main__":
    list1 = ["a", "b", "c"]
    list2 = [4, 5, 6]
    list3 = [7, 8, 9]

    result = combine_three_lists(list1, list2, list3)
    print("Combined List:", result)
