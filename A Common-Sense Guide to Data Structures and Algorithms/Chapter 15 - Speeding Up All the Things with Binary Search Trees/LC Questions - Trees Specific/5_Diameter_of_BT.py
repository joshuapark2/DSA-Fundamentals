'''
https://neetcode.io/problems/binary-tree-diameter?list=neetcode250
Should be a LC Medium because the complexity is that the returned value of height
is not the result, we need diameter instead.

Time Complexiy: O(n)
Space Complexity: O(h)
    Best Case balanced: O(log (n))
    Worst Case degenerate: O(n)

If you want to remove '.self' for variable result, just declare it as nonlocal

Algorithm:
    - 1. Post Order Traversal -> Left, Right Subtrees, Node
    - 2. Find Height
    - 3. Find Diameter
        Note that diameter is the furtherest length from the bottom child left and right
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def diameter(self, root):
    result = 0

    def algo(node):
        nonlocal result

        if not node:
            return 0

        left = algo(node.left)
        right = algo(node.right)

        # Height
        result = max(result, left + right)
        # Diameter
        return max(left, right) + 1
    
    algo(root)
    return result
'''
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

        self.result = max(self.result, left + right) # This is how we find height
        return max(left, right) + 1 # This is how we find diameter
    
    dfs(root)
    return self.result

How the algorithm works:
 - Reach base case of 0
    left = dfs(node.left) -> left = dfs(0) and right = dfs(0)
    self.result = max(self.result, 0 + 0)
    return max(0, 0) + 1

    root = [1,null,2,3,4,5]
    return max(1, 0) + 1
    return max(2, 0) + 1
    return max(3, 0) + 1
    return max(3, 1) + 1
    return max(3, 2) + 1
    return max(3, 3) -> diameter = 3 -> Output: 3
'''

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

'''
LC Solution
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(root):
            nonlocal res

            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            res = max(res, left + right)

            return 1 + max(left, right)

        dfs(root)
        return res
'''