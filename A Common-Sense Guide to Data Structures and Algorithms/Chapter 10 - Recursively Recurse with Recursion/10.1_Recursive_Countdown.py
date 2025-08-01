def recursive_count_down(number):
    print(number)
    if (number == 0):
        return
    else:
        recursive_count_down(number - 1)

recursive_count_down(10)