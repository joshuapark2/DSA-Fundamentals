'''
For questions such as 1_Maximum_Depth_BST.py, how does +1 work in the call stack?

Good Reference:
https://stackoverflow.com/questions/33977997/explain-how-recursion-works-in-an-algorithm-to-determine-depth-of-binary-tree
 - Essentially if we have 
    return max(leftHeight, rightHeight) + 1
   +1 is added to whatever variable is visited in the recursion stack
'''
def recursionStack(num):
    if not num:
        return 0
    num -= 1
    return recursionStack(num) + 1

print(recursionStack(3))

'''
So the way this works is that once we hit the base case, we retrace all our steps
with the returned value:
    Recursion:
        recursionStack(3) => recursionStack(2) + 1
        recursionStack(2) => recursionStack(1) + 1
        recursionStack(1) => recursionStack(0) + 1
        recursionStack(0) => 0

    Retrace Steps:
        (0)         - Base Case
        (0) + 1 = 1 - Prev step + current stack
        (1) + 1 = 2
        (2) + 1 = 3
        Ans: 3

Basically whatever value is returned will be replaced in our parameter variable
'''