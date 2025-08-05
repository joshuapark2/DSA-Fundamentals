'''
The following function accepts an array of numbers and returns the sum, as long as a particular number 
doesnt bring the sum above 100.
If adding a particular number will make the sum higher than 100, that number is ignored. 

However, this function makes unnecessary recursive calls. 
Fix the code to eliminate the unnecessary recursion:
'''
def add_until_100(array):
    if len(array) == 0:
        return 0

    array_reduced = add_until_100(array[1:])

    if array[0] + array_reduced > 100:
        return array_reduced
    else:
        print(array[0] + array_reduced)
        return array[0] + array_reduced

add_until_100([1, 2, 3, 4])

print()

def add_until_100_inefficient(array):
    if len(array) == 0:
        return 0
    if array[0] + add_until_100(array[1:]) > 100:
        return add_until_100(array[1:])
    else:
        print(array[0] + add_until_100(array[1:]))
        return array[0] + add_until_100(array[1:])
    
add_until_100_inefficient([1, 2, 3, 4])



# Scratch Sheet - Brainstorming
'''
Array of nums -> returns the sum as long as it doesn't go beyond 100
Otherwise - do the math


def add_until_100_Progress(array, memo = {}):
    if len(array) == 0:
        return 0

    sum_stored = array[0] + add_until_100_Progress(array[1:]) # Math to store key

    memo[sum_stored] = array # key:value pairs

    if not memo.get(sum_stored): # Conditional of if sum is not stored
        memo[sum_stored] = array # value is array

    return  memo[sum_stored]

def add_until_100_Progress(array, memo = {}):
    if len(array) == 0:
        return 0

    sum_stored = array[0] + add_until_100_Progress(array[1:])
    # We must do the sum_stored calculation inside if it doesn't exist yet

    if not memo[sum_stored]:
        memo[sum_stored] = array

    return memo[sum_stored]

def add_until_100_Progress(array, memo = {}):
    if len(array) == 0:
        return 0

    if not memo[sum_stored]:
        sum_stored = memo[array[0] + add_until_100_Progress(array[1:])]

        if sum_stored < 100:
            memo[sum_stored] = array
        else:
            return array[1:]

    return memo[sum_stored]

# Problem is that the calculation must be done before...
def add_until_100_Progress(array, memo = {}):
    if len(array) == 0:
        return 0

    sum_stored = memo[array[0] + add_until_100_Progress(array[1:])]

    if sum_stored < 100:
        return memo[sum_stored] = array
    else:
        return array[1:]

    return memo[sum_stored]


def add_until_100(array, memo = {}):
    if len(array) == 0:
        return 0

    sum_stored = memo[array[0] + add_until_100(array[1:])]

    if sum_stored < 100:
        memo[sum_stored] = array
        return memo[sum_stored]
        
    return memo[sum_stored]


add_until_100([1, 2, 3, 4])
'''