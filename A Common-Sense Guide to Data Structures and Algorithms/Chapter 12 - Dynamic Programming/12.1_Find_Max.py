# Find Greatest number from an array example

def find_max(array):
    # Base case: if there's only one element, return it
    if len(array) == 1:
        return array[0]
    
    # Recursive step: find the max of the rest of the array
    max_of_rest = find_max(array[1:])
    
    # Compare and return the greater value
    if array[0] > max_of_rest:
        return array[0]
    else:
        return max_of_rest

# Ineffient version below:
def find_max(array):
    if len(array) == 1:
        return array[0]
    
    # Ineffiency here
    if array[0] > find_max(array[1:]):
        return array[0]
    else:
        return find_max(array[1:])

# Little Fix:
def find_max(array):
    # Base case: if there's only one element, return it
    if len(array) == 1:
        return array[0]
    
    # Recursive step: find the max of the rest of the array
    max_of_rest = find_max(array[1:])
    
    # Compare and return the greater value
    if array[0] > max_of_rest:
        return array[0]
    else:
        return max_of_rest