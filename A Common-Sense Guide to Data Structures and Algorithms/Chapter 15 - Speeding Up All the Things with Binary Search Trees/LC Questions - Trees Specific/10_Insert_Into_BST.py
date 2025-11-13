# Link: https://neetcode.io/problems/insert-into-a-binary-search-tree?list=neetcode250
'''
Measured in n of nodes in tree or h for height of tree -> can be measured in different ways
    - Best case we can visit half, worst case is unbalanced -> Time complexity: O(h) is more accurate since h can be equal to n -> Height of the tree
    - Recursion call stack takes extra memory - Space Complexity O(h)
        - Iterative is just a pointer - Space O(1)
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def insertIntoBST(root, val):
    if not root:
        return TreeNode(val)

    if val > root.val:
        root.right = insertIntoBST(root.right, val)
    else:
        root.left = insertIntoBST(root.left, val)
    
    return root


'''
My Attempt

Problems:
    - 

Error: 
    return root.left = TreeNode(val)
                     ^
    SyntaxError: invalid syntax

class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        def insertion(root, val):
            if not val or not root:
                return None
            
            # Traversal
            if val <= root.val:
                return insertion(root.left, val)
            else:
                return insertion(root.right, val)
            
            # Placement
            if not root.left and val <= root.val:
                return root.left = TreeNode(val)
            elif not root.right and val > root.val:
                return root.right = TreeNode(val)
            else:
                return root
        
        insertion(root, val)
        return root

Breakdown:
    - Base case: Doesn't make sense to check for val because its guaranteed that the new value doesn't exist in the original BST
        And we need val to be an int for this problem to work, it cannot be None so 'if not val' doesn't make sense.
        - The goal for our base case isn't to return None, but rather the TreeNode which can only be created without a nested function.

    - Traversal: Since the new value is guaranteed that it doesn't exist in the original BST, we can simply to greater/less than.
        - The biggest question is how we're supposed to link it up from the parent node rather than the child node and
            root.left =
            root.right =
            ^ This is how we link from the parent node recursively and must return root at the end to avoid returnining None
'''