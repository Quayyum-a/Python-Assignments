def get_common(num1: list, num2: list) -> list:
    common = []
    for count in num1:
        if count in num2:
            common.append(count)
    return common


