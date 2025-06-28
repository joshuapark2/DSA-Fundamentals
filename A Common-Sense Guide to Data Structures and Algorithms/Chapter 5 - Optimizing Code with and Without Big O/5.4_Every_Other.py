def every_other(array):
    for index, number in enumerate(array):
        if index % 2 == 0:
            for other_number in array:
                print(number + other_number)