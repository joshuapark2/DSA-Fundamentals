
'''
Array Intersection Example: [3, 1, 4, 2] and [4, 5, 3, 6] = [3, 4]

Brute Force Example:
'''
def intersection(first_array, second_array):
    result = []
    for i in range(len(first_array)):
        for j in range(len(second_array)):
            if first_array[i] == second_array[j]:
                result.append(first_array[i])
    return result

# Optimization with a single word where we don't need to check if both index values are equal:
def intersection_optimized(first_array, second_array):
    result = []
    for i in range(len(first_array)):
        for j in range(len(second_array)):
            if first_array[i] == second_array[j]:
                result.append(first_array[i])
                break
    return result
