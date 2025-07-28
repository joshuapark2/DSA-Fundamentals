'''
Write a function that returns the intersection of two arrays. 
The intersection is a third array that contains all values contained within the first two arrays. 

For example, the intersection of [1, 2, 3, 4, 5] and [0, 2, 4, 6, 8] is [2, 4]. 
Your function should have a complexity of O(N). 
(If your programming language has a built-in way of doing this, don’t use it. The idea is to build the algorithm yourself.)
'''

'''
Write a function that returns the intersection of two arrays. 
The intersection is a third array that contains all values contained within the first two arrays. 

For example, the intersection of [1, 2, 3, 4, 5] and [0, 2, 4, 6, 8] is [2, 4]. 
Your function should have a complexity of O(N). 
(If your programming language has a built-in way of doing this, don’t use it. The idea is to build the algorithm yourself.)
'''

def intersection_array(array1, array2):
	# Intersection Array
	intersectionArray = []

	# Hashmap with truthy value for values
	hashmap = {}

	for value in array1:
		hashmap[value] = True
	# {0: True, 2: True, 4: True, 6: True, 8: True}

	# If smaller array in big array, put into third array that intersect
	for value in array2:
		if value in hashmap:
			intersectionArray.append(value)

	print(intersectionArray) # [2, 4]
	return intersectionArray

intersection_array([1, 2, 3, 4, 5], [0, 2, 4, 6, 8])

'''
VERSION 1:
def intersection_array(array1, array2):
	# Bigger and Smaller Array
	biggerArray, smallerArray, intersectionArray = [], [], []

	if len(array1) > len(array2):
		biggerArray = array1
		smallerArray = array2
	else:
		biggerArray = array2
		smallerArray = array1

	# Hashmap with truthy value for values
	hashmap = {}

	for value in biggerArray:
		hashmap[value] = True
	# {0: True, 2: True, 4: True, 6: True, 8: True}

	# If smaller array in big array, put into third array that intersect
	for value in smallerArray:
		if value in hashmap:
			intersectionArray.append(value)

	print(intersectionArray) # [2, 4]
	return intersectionArray
'''

intersection_array([1, 2, 3, 4, 5], [0, 2, 4, 6, 8])