'''
https://neetcode.io/problems/binary-tree-diameter?list=neetcode250
Should be a LC Medium because the complexity is that the returned value of height
is not the result, we need diameter instead.

Time Complexiy: O(n)
Space Complexity: O(h)
    Best Case balanced: O(log (n))
    Worst Case degenerate: O(n)

If you want to remove '.self' for variable result, just declare it as nonlocal
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def diameter(self, root):
    # '.self' required to create a membered variable to be accessible in our 
    # nested function
    self.result = 0 # or nonlocal result = 0 and remove all .self for this var

    # Return height
    def dfs(node):
        if not node:
            return 0
        left = dfs(node.left)
        right = dfs(node.right)

        self.result = max(self.res, left + right) # This is how we find height
        return max(left, right) + 1 # This is how we find diameter
    
    dfs(root)
    return self.result

'''
Shorthand: return max(self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right)) + 1
but root=[1,null,2,3,4,5] edge case doesn't work

My original attempt below:def diameter(self, root):
    if not root:
        return 0

    left = self.diameterOfBinaryTree(root.left) + 1
    right = self.diameterOfBinaryTree(root.right) + 1

    answer = max(left, right)
    return answer
'''