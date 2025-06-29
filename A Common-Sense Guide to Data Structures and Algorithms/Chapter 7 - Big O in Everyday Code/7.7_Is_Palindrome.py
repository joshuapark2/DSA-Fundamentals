'''
Determine if string is Palindrome 
- A palindrome is a word or phrase that reads the same both forward and backward.

Some examples include “racecar,” “kayak,” and “deified.”
'''

def is_palindrome(string):
    # Start the leftIndex at index 0:
    left_index = 0
    # Start rightIndex at last index of array:
    right_index = len(string) - 1
    # Iterate until leftIndex reaches the middle of the array:
    while left_index < len(string) / 2:
        # If the character on the left doesn't equal the character
        # on the right, the string is not a palindrome:
        if string[left_index] != string[right_index]:
            return False
        # Move leftIndex one to the right:
        left_index += 1
        # Move rightIndex one to the left:
        right_index -= 1
    # If we got through the entire loop without finding any
    # mismatches, the string must be a palindrome:
    return True
