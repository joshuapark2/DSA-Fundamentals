def anagrams_of(string):
  if len(string) == 1:
    return [string[0]]

  collection = []

  substring_anagrams = anagrams_of(string[1:])

  for substring_anagram in substring_anagrams:
    for index in range(len(substring_anagram) + 1):
      new_anagram = substring_anagram[:index] + string[0] + substring_anagram[index:]
      collection.append(new_anagram)

  return collection



# With Comments Below

def anagrams_of(string):
  # Base case: if the string is only one character,
  # return a list containing just that character
  if len(string) == 1:
    return [string[0]]

  # Create a list to hold all the anagrams
  collection = []

  # Get all anagrams of the substring starting from the second character
  substring_anagrams = anagrams_of(string[1:])

  # Iterate over each anagram of the substring
  for substring_anagram in substring_anagrams:
    # Insert the first character at every possible position
    for index in range(len(substring_anagram) + 1):
      # Create a new string with the character inserted
      new_anagram = substring_anagram[:index] + string[0] + substring_anagram[index:]
      # Add the new string to the collection
      collection.append(new_anagram)

  # Return the full list of anagrams
  return collection

