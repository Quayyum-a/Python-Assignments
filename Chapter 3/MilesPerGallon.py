totalMiles = 0
totalGallons = 0
count = 1

while count == 1:
   miles = float(input('Enter the miles driven: '))
   totalMiles += miles

   gallons = float(input('Enter the gallons used: '))
   totalGallons += gallons
   total = totalMiles / totalGallons
   print('The miles/gallon for this tank was', total)

   print('\nDo you want to continue adding data?')

   count = float(input('\nEnter 1 to continue and -1 to end '))

if count == -1:
    print('Done!')