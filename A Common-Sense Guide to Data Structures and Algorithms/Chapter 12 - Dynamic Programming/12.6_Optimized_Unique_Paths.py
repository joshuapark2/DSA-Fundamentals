'''
Here is a solution to the “Unique Paths” problem from an exercise in the previous chapter. 
Use memoization to improve its efficiency:

 Textbook: 
  To accomplish memoization here, 
  we need to make a key out of both the number of rows and number of columns. 
  We can make our key a simple array of [rows, columns]:
'''
def unique_paths(rows, columns, memo={}):
    if rows == 1 or columns == 1:
        return 1
    if (rows, columns) not in memo:
        memo[(rows, columns)] = unique_paths(rows - 1, columns, memo) + unique_paths(rows, columns - 1, memo)
    return memo[(rows, columns)]


def unique_paths_na(rows, columns):
    if rows == 1 or columns == 1:
        return 1
    return unique_paths_na(rows - 1, columns) + unique_paths_na(rows, columns - 1)

# My version
def unique_path(rows, columns, memo = {}):
    if rows == 1 or columns == 1:
        return 1

    total = (rows - 1 + columns) + (rows + columns - 1)

    if not memo.get(total):
        memo[total] = unique_path(rows - 1, columns) + unique_path(rows, columns - 1)

    return memo[total]

print(unique_path(3, 3))
print()
print(unique_paths_na(3, 3))