def contains_x(string):
    found_x = False
    for i in range(len(string)):
        if string[i] == "X":
            found_x = True
    return found_x

def contains_x_optimized(string):
    for i in range(len(string)):
        if string[i] == "X":
            return True
    return False