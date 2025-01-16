input1 = int(input('Enter integer 1: '))
input2 = int(input('Enter integer 2: '))
input3 = int(input('Enter integer 3: '))
input4 = int(input('Enter integer 4: '))

sum = (input1 + input2 + input3 + input4)
print(sum, "is the sum of the integers")

average = sum / 3
print("\nThe average of the integers is ", average)

product = input1 * input2 * input3 + input4
print("\nThe product of the integers is ", product)

largest = input1 
if largest < input2 :
    largest = input2
elif largest < input3 :
    largest = input3
elif largest < input4:
    largest = input4
print("\nThe largest integer is ", largest)
smallest = input1

if smallest > input2 :
    smallest = input2
elif smallest > input3 :
    smallest = input3
elif smallest > input4 :
    smallest = input4
    
print("\nThe smallest integer is ", smallest)
