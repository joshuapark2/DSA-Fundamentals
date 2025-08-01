def number_of_paths(n):
    if n < 0:
        return 0
    elif n == 1 or n == 0:
        return 1
    return number_of_paths(n - 1) + number_of_paths(n - 2) + number_of_paths(n - 3)

# Print example
def number_of_paths(n, depth=0):
    indent = "  " * depth  # indent to visualize call depth
    print(f"{indent}number_of_paths({n}) called")

    if n < 0:
        print(f"{indent}Returning 0 (n < 0)")
        return 0
    elif n == 0 or n == 1:
        print(f"{indent}Returning 1 (base case)")
        return 1

    result = (
        number_of_paths(n - 1, depth + 1) +
        number_of_paths(n - 2, depth + 1) +
        number_of_paths(n - 3, depth + 1)
    )

    print(f"{indent}Returning {result} for n = {n}")
    return result

# Example usage
number_of_paths(2)
