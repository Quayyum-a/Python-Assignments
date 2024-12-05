#2.4 ODD AND EVEN ASSIGNMENT

count = 0

while count <= 10:
	count += 1
	number = int(input(f"Enter integer {count}: "))
	if number % 2 == 0:
		print(f"The number {number} is an even number")
	else:
		print(f"The number {number} is an odd number")