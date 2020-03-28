def arithmeticSequence(initialTerm, commonDifference, numTerms):
	sequence = ''
	for i in range(initialTerm, (initialTerm + (numTerms*commonDifference)), commonDifference):
		sequence = sequence + ', ' + str(i)
	return sequence[2:]

print(arithmeticSequence(2,5,6))

def multiplesList(n, startingNum, endingNum):
	multiplesString = ''
	for i in range(startingNum, endingNum + 1):
		if i % n == 0:
			multiplesString = multiplesString + ", " + str(i)
	return multiplesString[2:]

print(multiplesList(3, 5, 15))

def fizzBuzzUpTo(n):
	output = ''
	for i in range(1, n + 1):
		if i % 3 == 0 and i % 5 == 0:
			output = output + '\nFizzBuzz'
		elif i % 3 == 0:
			output = output + '\nFizz'
		elif i % 5 == 0:
			output = output + '\nBuzz'
		else:
			output = output + '\n' + str(i)
	return output[1:]

print(fizzBuzzUpTo(16))