class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

'''
Inorder traversal goes left, center, right 
- meaning we go all the way to the left until we reach our base case which is when a node is None.
- Then we check the val and append to our array
- Lastly we check right

Version 1 Below Attempt 10/30/25

def inorderTraversal(node):
    answer = []

    if not node:
        return None
    
    def algorithm(node):
        algorithm(node.left)
        answer.append(node.val)
        algorithm(node.right)
    algorithm(node)
    return answer

Commentary:
    1. root is a better name than node and can be acceesed in our nested function
        due to scope
    2. Base case will always go inside our algorithm, doesn't make sense otherwise
    3. Main concept here is basic recursion and functional scope
'''

def inorderTraversal(root):
    result = []

    def algorithm(node):
        if not node:
            return None
        algorithm(node.left)
        result.append(node.val)
        algorithm(node.right)

    algorithm(root)
    return result