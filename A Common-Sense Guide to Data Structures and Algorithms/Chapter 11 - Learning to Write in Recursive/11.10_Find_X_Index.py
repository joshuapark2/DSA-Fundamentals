'''
Use recursion to write a function that accepts a string and returns the first index that contains the character “x.” 
    For example, the string, "abcdefghijklmnopqrstuvwxyz" has an “x” at index 23. 
    To keep things simple, assume the string definitely has at least one “x.”
'''

def find_x(string):
    if string[0] == "x":
        return 0
    return find_x(string[1::]) + 1


'''

Assume that the function is already done for you
what is the sub-problem
what happens if you put the subproblem within the function

'a' + find_x('bcdefghijklmnopqrstuvwxyz')

find_x(string[1::]) + 1

base case: 'x'
'''