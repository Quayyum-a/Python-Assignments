entry1 = input('What is your problem? ')

entry2 = input('\nHave you had this problem before? ').lower()

if entry2 == 'yes' :
    print('\nWell, you have it again')
if entry2 == 'no' :
    print('\nWell, you have it now')