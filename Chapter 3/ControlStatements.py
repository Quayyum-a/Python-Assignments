largest = float("-inf")  
secondlargest = float("-inf")  


for _ in range(10):
    number = int(input("Enter a number: "))
    
    if number > largest:
        secondlargest = largest
        largest = number
        
    elif number > secondlargest:
        secondlargest = number
print(f"The largest number is: {largest}")
print(f"The second largest number is: {secondlargest}")
