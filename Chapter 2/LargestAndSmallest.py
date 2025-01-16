input1 = int(input('Enter integer 1: '))
input2 = int(input('Enter integer 2: '))
input3 = int(input('Enter integer 3: '))

sum = (input1 + input2 + input3)
print(sum, "is the sum of the integers")

average = sum / 3
print("The average of the integers is ", average)

product = input1 * input2 * input3
print("The product of the integers is ", product)

largest = input1 
if largest < input2 :
    largest = input2
if largest < input3 :
    largest = input3
print("The largest integer is ", largest)
smallest = input1

if smallest > input2 :
    smallest = input2
if smallest > input3 :
    smallest = input3
print("The largest integer is ", smallest)
