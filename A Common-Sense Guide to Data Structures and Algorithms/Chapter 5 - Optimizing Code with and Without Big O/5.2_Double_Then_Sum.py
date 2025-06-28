def double_then_sum(array):
    doubled_array = []
    for number in array:
        doubled_array.append(number * 2)

    total = 0
    for number in doubled_array:
        total += number

    return total