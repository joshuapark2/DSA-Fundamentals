# 1. Initalize a single node
class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def nodeInfo(node):
    return print(node.val, node.left, node.right)
    
'''
    Below is same as:
        node2 = node1.left = TreeNode(4)
        node3 = node1.right = TreeNode(6)
'''
node1 = TreeNode(5, TreeNode(4), TreeNode(6))
nodeInfo(node1)

# Inorder Traversal printed
def recursivePrint(root):
    if not root:
        return None

    recursivePrint(root.left)
    print(root.val)
    recursivePrint(root.right)

#recursivePrint(node1)

# Adding array to make the print output clearner
# Note array doesn't need nonlocal because it's mutable vs. string that's immutable
# keywork nonlocal allows the data type to become mutable
def recursiveArray(root):
    array = []

    def inorder(node):
        if not node:
            return None
        
        inorder(node.left)
        array.append(node.val)
        inorder(node.right)

    inorder(root)
    return print(array)

recursiveArray(node1)