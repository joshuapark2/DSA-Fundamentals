'''
if not x evaluates whether the variable x is "falsy"
Meaning if x evaluates to False in a boolean context.

Examples:
 - False
 - None
 - Numeric zero of any type: 0, 0.0, 0j
 - Empty sequences: '', [], (), b''
 - Empty Mappings: {}
 - Empty sets: set()
'''

x = []
if not x:
    print('x is empty')

y = 0
if not y:
    print('y is zero')

z = None
if not z:
    print('z is None')

name = 'Alice'
if not name:
    print('name is empty') # Won't print sine 'Alice' is not falsy

'''
if not x vs. if x is None biggest differences
    - if not x will check for other falsy values
    - if x is None will only check if x is the None object
'''
my_list = []
if not my_list:
    print('List is falsy (empty)') # Will be printed

if my_list is None:
    print("List is None") # Won't be printed