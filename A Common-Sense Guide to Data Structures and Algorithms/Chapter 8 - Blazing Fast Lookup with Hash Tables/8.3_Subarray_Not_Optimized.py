# Valid
subsetA = ['a', 'b', 'c', 'd', 'e', 'f']
subsetB = ['b', 'd', 'f']

# Invalid w/ subsetA
subsetC = ['b', 'd', 'f', 'h']
subsetD = ['j', 'f']

def is_subset(array1, array2):
	largerArray, smallerArray = [], []

	if len(array1) > len(array2):
		largerArray = array1
		smallerArray = array2
	else:
		largerArray = array2
		smallerArray = array1

	for l1 in smallerArray:
		foundMatch = False
		for l2 in largerArray:
			if l1 == l2:
				foundMatch = True
				break
		if foundMatch == False:
			return False
	print(foundMatch)


is_subset(subsetA, subsetC)