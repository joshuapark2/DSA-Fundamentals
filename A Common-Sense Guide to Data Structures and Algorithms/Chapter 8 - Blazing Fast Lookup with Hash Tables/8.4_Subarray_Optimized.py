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

	hashmap = {}

	for value in largerArray:
		hashmap[value] = True
		# {'a': True, 'b': True, 'c': True, 'd': True, 'e': True, 'f': True}

	for value in smallerArray:
		if value not in hashmap:
			return False
	return True


is_subset(subsetA, subsetB)