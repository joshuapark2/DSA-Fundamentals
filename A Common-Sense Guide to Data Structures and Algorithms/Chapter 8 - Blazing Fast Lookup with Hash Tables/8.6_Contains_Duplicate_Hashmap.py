'''
Write a function that accepts an array of strings and returns the first duplicate value it finds. 

For example, if the array is ["a", "b", "c", "d", "c", "e", "f"], 
	the function should return "c", since it’s duplicated within the array. 
	(You can assume that there’s one pair of duplicates within the array.) 

Make sure the function has an efficiency of O(N).
'''

def contains_duplicate(array):
	hashmap = {}

	for value in array:
		if value in hashmap:
			print('duplicate: ', value)
			return value
		hashmap[value] = True
	print('no duplicates')
	return hashmap

contains_duplicate(["a", "b", "c", "d", "c", "e", "f"])