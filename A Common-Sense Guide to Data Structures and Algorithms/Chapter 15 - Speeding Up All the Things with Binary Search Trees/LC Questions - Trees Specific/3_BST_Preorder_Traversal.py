'''
Preorder traversal can be defined as node itself, left and right subtrees
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def preorderTraversal(root):
    answer = []

    def preorder(node):
        if not node:
            return None
        answer.append(node.val)
        preorder(node.left)
        preorder(node.right)
    
    preorder(root)
    return answer

'''
AttributeError: 'NoneType' object has no attribute 'val'
root=[1,2,3,4,5,6,7]

Fix: Replace root on line 33, with node
'''
def preorderTraversalV1(root):
    answer = []

    def algorithm(node):
        if not root: # Should be node, not root
            return None
        answer.append(node.val)
        algorithm(node.left)
        algorithm(node.right)
    
    algorithm(root)
    return answer