'''
Write a function that accepts a string that contains all the letters of the alphabet except one and returns the missing letter. 

For example, the string, "the quick brown box jumps over a lazy dog" contains all the letters of the alphabet except the letter, "f". 

The function should have a time complexity of O(N).
'''

def missing_alphabet(phrase):
	# create a hashmap containing all letters of the alphabet
	hashmap = {}
	filteredString = ""

	# 1.1 use ord() and each value is associated with a key
	# a = 97, z = 122, range from 0 to 25
	for i in range(97, 123):
		hashmap[i] = 0

	# filter string
	for letter in phrase:
		'''
		if letter.isalpha():
			filteredString += letter
		'''
		if ord(letter) >= 97 and ord(letter) <= 122:
			filteredString += letter

	# Next if the ord(letter) within phrase, +1 count to hashmap
	for letter in filteredString:
		hashmap[ord(letter)] = hashmap.get(0, ord(letter)) - ord(letter) + 1

	# lastly any value that is 0, we get the key and return the one missing letter
	for n in hashmap:
		if hashmap[n] == 0:
			print(chr(n))
			return chr(n)

missing_alphabet("the quick brown box jumps over a lazy dog")