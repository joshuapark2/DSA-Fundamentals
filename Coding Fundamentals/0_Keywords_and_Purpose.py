# Abs to find the difference and equate to positive
absolute = abs(1 - 2) # Output: 1

# nonlocal - https://www.w3schools.com/python/ref_keyword_nonlocal.asp
# Make a function inside a function, use a variable from it's outer scope
# /Scope/0_nonlocal.py for more details
def funct1():
    name = "John"
    def funct2():
        nonlocal name
        name = "Harry"
    funct2()
    return name

print(funct1()) # Output: Harry