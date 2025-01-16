passes = 0 
failures = 0 
counter = 0

for student in range(10):
   result = int(input('Enter result (1=pass, 2=fail): '))
    
   while (result > 1):
      if result == 1:
      passes = passes + 1
      counter += passes
      else:
      failures = failures + 1


print('Passed:', passes)
print('Failed:', failures)

if passes > 8:
    print('Bonus to instructor')