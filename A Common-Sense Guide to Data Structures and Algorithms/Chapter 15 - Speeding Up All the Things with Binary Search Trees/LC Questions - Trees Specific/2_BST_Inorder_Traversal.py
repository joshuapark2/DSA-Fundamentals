from collections import deque
'''
Inorder Traversal for BST start from subtree left, center, right
O(n) - time complexity due to recursion and visiting every ndoe
o(n) - using function call stack
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
def inorderTraversalRecursion(root):
    result = []

    def inorder(node):
        # Base Case
        if not node:
            return
        inorder(node.left)
        result.append(node.val)
        inorder(node.right)
    
    inorder(root)
    return result

def print_tree(node, level=0, prefix="Root: "):
    if node:
        print("    " * level + prefix + str(node.val))
        if node.left or node.right:
            print_tree(node.left, level + 1, "L--- ")
            print_tree(node.right, level + 1, "R--- ")

def build_tree(array):
    if not array or array[0] is None:
        return None

    root = TreeNode(array[0])
    queue = deque([root])
    i = 1

    while queue and i < len(array):
        current = queue.popleft()

        # Left Child
        if i < len(array) and array[i] is not None:
            current.left = TreeNode(array[i])
            queue.append(current.left)
        i += 1

        if i < len(array) and array[i] is not None:
            current.right = TreeNode(array[i])
            queue.append(current.right)
        i += 1
    
    return root

root = build_tree([1, 2, 3, 4, 5, None, None, 6, 7, 9])
# Output: [4,2,6,5,7,1,3,9,8]
inorderTraversalRecursion(root)
print_tree(root)