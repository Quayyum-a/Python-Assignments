numbers = [9, 11, 22, 34, 17, 22, 34, 22, 40]

sum1 = sum(numbers)


mean1 = sum1 / len(numbers)

print("The mean of the numbers is:", mean1)


sum2 = sum1 + 34


mean2 = sum2 / (len(numbers) + 1)

print("With another number (34), the mean is:", mean2)
print("")

