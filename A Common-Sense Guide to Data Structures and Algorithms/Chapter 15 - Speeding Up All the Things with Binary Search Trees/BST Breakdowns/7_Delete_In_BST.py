'''
https://www.geeksforgeeks.org/dsa/deletion-in-binary-search-tree/#

Deleting in BST depends on its number of children nodes and has three possibilities:
    1. No children = Simply remove
    2. One Child = Remove node + connect to parent node
    3. Two Children = Replace node with inorder successor/predecessor and delete
        - Successor is smallest value in right subtree that's greater than target node (basically next largest value)
        - Predecessor is largesst value in the left subtree that's less than target node (basically next smallest value)
'''

class NodeTree:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Method with Successor - next largest value compared to target
def getSuccessor(node):
    node = node.right
    while node is not None and node.left is not None:
        node = node.left
    return node

def deleteNode(node, target):
    if node is None:
        return node
    
    if node.left > target:
        node.left = deleteNode(node.left, target)
    elif node.data < target:
        node.right = deleteNode(node.right, target)
    else:
        # node w/ 0 or 1 children
        if node.left is None:
            return node.right
        if node.right is None:
            return node.left
        
        # Node w/ 2 children
        successor = getSuccessor(node)
        node.val = successor.val
        node.right = deleteNode(node.right, successor.val)
    
    return node