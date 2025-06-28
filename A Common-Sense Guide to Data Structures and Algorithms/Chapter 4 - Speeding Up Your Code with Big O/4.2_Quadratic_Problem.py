def hasDuplicateValue(array):
    steps = 0
    for i in range(len(array)):
        for j in range(len(array)):
            steps += 1
            if i != j and array[i] == array[j]:
                return True
    print(steps)
    return False

print(hasDuplicateValue([1,2,3, 4, 5]))

def has_duplicate_value(array):
    seen = set()
    for value in array:
        if value in seen:
            return True
        seen.add(value)
    return False
