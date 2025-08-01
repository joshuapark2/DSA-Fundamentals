def sum(array, index = 0, product = 1):
    if index >= len(array):
        return product
    else:
        product += array[index]
        sum(array, index + 1, product)


def simple_sum(array):
    # Base case: only one element in the array
    if len(array) == 1:
        return array[0]
    return array[0] + sum(array[1 : len(array) - 1]) # or array[1:]

sum([1, 2, 3, 4, 5])
simple_sum([1, 2, 3, 4, 5])