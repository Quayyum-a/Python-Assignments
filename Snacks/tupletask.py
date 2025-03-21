import random
numbers = ()
odd_position = 0
even_position = 0

for _ in range(20):
    numbers += (random.randint(1, 100),)

for count, num in enumerate(numbers):
    if count % 3 == 0:
        odd_position += num

    if count % 2 == 0:
        even_position += num

    max_num = max(numbers)
    min_num = min(numbers)
sum = max_num + min_num

product_of_first_five = 1
for num in numbers[:5]:
    product_of_first_five *= num

print("The sum of odd position is ", odd_position)
print("The sum of even position is ", even_position)
print("The sum of the smallest and highest numbers is ", sum)
print("The product of the first five integers is", product_of_first_five)