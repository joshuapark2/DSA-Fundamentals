'''


Array Given: [1, 2, 3, 4, 5]
Array Result: [2, 3, 4, 5, 6, 8, 10, 12, 15, 20]
'''

def two_number_products(array):
    products = []
    # Outer array:
    for i in range(len(array) - 1):
        # Inner array, in which j always begins one index
        # to the right of i:
        for j in range(i + 1, len(array)):
            products.append(array[i] * array[j])
    return products
