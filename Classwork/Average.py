print('Scores for 10 students')

count = 1
total = 0

highest = 0
lowest = 0



while count <= 10:
	score =	float(input('Enter Integer: '))
	total += score	

	if count == 1:
		highest = score
		lowest = score

	else:
		if score > highest:
 			highest = score
	if score < lowest:
        	lowest = score  

	count += 1


average = total / 10
range = highest - lowest

print('The total of all the numbers is', total)
print('The average of all the numbers is', average)
print('The highest of all the numbers is', highest)
print('The lowest of all the numbers is', lowest)
print('The Range of all the numbers is', range)