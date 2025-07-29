'''
Write a function that uses a stack to reverse a string. (For example, "abcde" would become "edcba".) 
You can work with our earlier implementation of the Stack class.
'''

def reverse_word(word):
    array = []

    for letter in word[::-1]:
        array.append(letter)

    print(array)

reverse_word('abcde')
print()

def reverse_stack(word):
    stack = []

    for letter in word:
        stack.append(letter)

    new_string = ""
    
    while len(stack) > 0:
        new_string += stack.pop()

    print(new_string)

reverse_stack('abcde')