# Finalized My Version
def count_x(string, count=0):
    if len(string) == 0:
        return 0
    elif string[0] == 'x':
        return count_x(string[1:], count + 1)
    else:
        return count_x(string[1:], count)

count_x('axbxcxdx')

# Finalized Textbook Version:
def count_x(string):
    # Base case: an empty string
    if len(string) == 0:
        return 0

    if string[0] == "x":
        return 1 + count_x(string[1:])
    else:
        return count_x(string[1:])




# My Version: Explicit Tracking
def count_x(string, count=0):
    if len(string) == 1:
        if string[0] == 'x':
            count += 1
        return count
    elif string[0] == 'x':
        return count_x(string[1:], count + 1)
    else:
        return count_x(string[1:], count)

# Textbook: Implicit Tracking
def count_x(string):
    # Base case
    if len(string) == 1:
        if string[0] == "x":
            return 1
        else:
            return 0

    if string[0] == "x":
        return 1 + count_x(string[1:])
    else:
        return count_x(string[1:])

# Textbook Simplified:
def count_x(string):
    # Base case: an empty string
    if len(string) == 0:
        return 0

    if string[0] == "x":
        return 1 + count_x(string[1:])
    else:
        return count_x(string[1:])

# Textbook Simplified w/ print statements -> Converting function object into a variable
def count_x(string):
    print(f"Called with: '{string}'")

    # Base case: an empty string
    if len(string) == 0:
        print(f"Base case reached with empty string → returning 0")
        return 0

    if string[0] == "x":
        result = 1 + count_x(string[1:])
        print(f"Found 'x' at '{string[0]}', adding 1 → returning {result} for '{string}'")
        return result
    else:
        result = count_x(string[1:])
        print(f"No 'x' at '{string[0]}' → returning {result} for '{string}'")
        return result

# Example usage
# count_x('axbxcxdx')
