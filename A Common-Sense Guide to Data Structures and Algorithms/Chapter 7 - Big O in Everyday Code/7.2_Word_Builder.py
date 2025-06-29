'''
Creates every combination of two character strings built from an array of single characters
Given Array: ['a', 'b', 'c', 'd']

Result Array: ['ab', 'ac', 'ad', 'ba', 'bc', 'bd', 'ca', 'cb', 'cd', 'da', 'db', 'dc']
'''

def word_builder(array):
    collection = []
    for i in range(len(array)):
        for j in range(len(array)):
            if i != j:
                collection.append(array[i] + array[j])
    return collection

# Three Characters
def word_builder(array):
    collection = []
    for i in range(len(array)):
        for j in range(len(array)):
            for k in range(len(array)):
                if i != j and j != k and i != k:
                    collection.append(array[i] + array[j] + array[k])
    return collection
