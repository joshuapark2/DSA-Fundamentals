'''
Level Order Traversal (Breadth First Search) of Binary Tree
https://www.geeksforgeeks.org/dsa/level-order-tree-traversal/
Level Order Traversal technique is a method to traverse a Tree such 
    that all nodes present in the same level are traversed completely 
    before traversing the next level.
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
def levelOrderTraversal(root, level, result):
    # Base Case:
    if not root:
        return # same as return None

    # Add a new level to the result if needed
    if len(result) <= level:
        result.append([])
    
    # Add current node.s data to its corresponding level
    result[level].append(root.val)

    # Recursively repeat for left and right children
    levelOrderTraversal(root.left, level + 1, result)
    levelOrderTraversal(root.right, level + 1, result)

# Function to perform level order traversal
def levelOrder(root):
    # Stores the result level by level
    result = []
    levelOrderTraversal(root, 0, result)
    return result

if __name__ == '__main__':
    #      5
    #     / \
    #   12   13
    #   /  \    \
    #  7    14    2
    # /  \  /  \  / \
    #17  23 27 3 8  11

    root = TreeNode(5)
    root.left = TreeNode(12)
    root.right = TreeNode(13)

    root.left.left = TreeNode(7)
    root.left.right = TreeNode(14)

    root.right.right = TreeNode(2)

    root.left.left.left = TreeNode(17)
    root.left.left.right = TreeNode(23)

    root.left.right.left = TreeNode(27)
    root.left.right.right = TreeNode(3)

    root.right.right.left = TreeNode(8)
    root.right.right.right = TreeNode(11)

    result = levelOrder(root)

    for level in result:
        print(' '.join(map(str, level)))
'''
Output: [[5], [12, 13], [7, 14, 2], [17, 23, 27, 3, 8, 11]]
Explanation:  Start with the root - [5]
Level 1: [12, 13]
Level 2: [7, 14, 2]
Level 3: [17, 23, 27, 3, 8, 11]

What's Printed:
5
12 13
7 14 2
17 23 27 3 8 11
'''