'''
Use recursion to write a function that accepts an array of strings and returns the total number of characters across all the strings. 
For example, if the input array is ["ab", "c", "def", "ghij"], the output should be 10 since there are 10 characters in total.

- Helpful thought process when learning to think in the top-down perspective broken down into three thoughts:
    1. Imagine the function you’re writing has already been implemented by someone else
    2. Identify the subproblem of the problem
    3. See what happens when you call the function on the subproblem and go from there
'''
def string_count(array):
    if len(array) == 1:
        return len(array[0])
    
    return len(array[0]) + string_count(array[1:])


def string_count_unrevised(array):
    if len(array) == 1:
        print(len(array[0]))
        return len(array[0])
    print(len(array[0]) + string_count_unrevised(array[1:]))
    return len(array[0]) + string_count_unrevised(array[1:])

string_count(['ab', 'c', 'def', 'ghij'])


'''
['ab', 'c', 'def', 'ghij'] -> 'ab' + ['c', 'def', 'ghij']

len(array[0]) + string_count(array[1:]))


2 + ['c', 'def', 'ghij']

2 + 1 + ['def', ghij]
2 + 1 + 3 + [ghij]

if len(array) == 1:
    return array[0]
'''