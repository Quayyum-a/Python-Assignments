integer1 = int(input("\nEnter 4 to confirm the multiple of 1024: "))
print("\n4 x 4 x 4 x 4 x 4 = 1024")

multiple1 = integer1 % 4

if integer1 % 4 == 0:
	print(f"\n So 4 is a multiple of 1024")

integer2 = int(input("\nEnter 2 to confirm the multiple of 10: "))
print("\n 2 x 2 x 2 x 2 = 16")
print("\n 2 x 2 x  = 8")


if integer2 % 2 == 0:
	print("\n So 2 is not a multiple of 10")