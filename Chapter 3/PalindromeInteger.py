integer = int(input('Enter a five digit number: '))

extractone = integer // 10000
extracttwo = (integer % 10000) // 1000
extractfour = (integer % 100) // 10 
extarctfive = integer % 10

if extractone == extarctfive :
    print(integer, ":  is a Palindrome integer!")
else :
    print('It is not a palindrome integer')