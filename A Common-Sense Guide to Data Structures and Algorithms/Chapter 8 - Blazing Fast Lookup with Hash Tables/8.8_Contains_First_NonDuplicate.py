def first_non_duplicate(word):
	hashmap = {}

	for letter in word:
		hashmap[letter] = hashmap.get(letter, 0) + 1
	print(dict(hashmap))

	for letter in hashmap:
		if hashmap[letter] == 1:
			print(letter)
			return letter

first_non_duplicate("minimum")