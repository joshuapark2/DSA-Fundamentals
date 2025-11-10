'''
Postorder traversal can be defined as first traversing left, right subtrees, then visiting node itself
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
def postorderTraversal(root):
    answer = []

    def postorder(node):
        if not node:
            return None

        postorder(node.left)
        postorder(node.right)
        answer.append(node.val)
    
    postorder(root)
    return answer

