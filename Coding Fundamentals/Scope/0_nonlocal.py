'''
https://www.w3schools.com/python/ref_keyword_nonlocal.asp
The nonlocal keyword is used to work with variables inside nested functions, where the variable should not belong to the inner function.
Use the keyword nonlocal to declare that the variable is not local.

JavaScript:
    - var (function scope) hoisted to the top and allowed usage in nested but not outer - global if not defined at a function
    - let (block scope) reassigned but not redeclared at only its own block{}
    - const (Block scope, but no reassigned nor redeclared) - but property can be changed for objects or arrays, just not the variable itself/naming
'''

def scope_1():
    name = "John"

    def scope_2():
        nonlocal name
        name = "Jessica"
    
    scope_2()
    return name
print(scope_1()) # Output: Jessica

def scope_no_nonlocal():
    name = "John"

    def scope_2():
        name = "Harry"
    
    scope_2()
    return name
print(scope_no_nonlocal()) # Output: John