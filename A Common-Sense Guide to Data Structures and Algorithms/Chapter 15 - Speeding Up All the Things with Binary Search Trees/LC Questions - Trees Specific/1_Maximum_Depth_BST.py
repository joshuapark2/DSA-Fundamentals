'''
A binary tree's maximum depth is the number of nodes along the longest path from 
  the root node down to the farthest leaf node.

Time Complexity = O(n) due to single traversal (depth-first search)
Space Complexity = O(n) for skewed/unbalanced or O(log n) for balanced since the space complexity is the size of our call stack
'''
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

  def __repr__(self):
    return f"TreeNode(val={self.val}, left={self.left}, right={self.right})"

  def maxDepth(self, root):
      if not root:
          return 0
      
      leftHeight = self.maxDepth(root.left)
      rightHeight = self.maxDepth(root.right)
      
      return max(leftHeight, rightHeight) + 1
'''
def maxDepth(root):
    def findHeight(node):
        if not node:
            return 0
        # Recursively find the height of the left and right subtrees
        leftHeight = findHeight(node.left)
        rightHeight = findHeight(node.right)
        return max(leftHeight, rightHeight) + 1
    return findHeight(root)
'''

# NeetCode solution below
def maxDepth_NeetCode(root):
  if not root:
    return 0

  return 1 + max(maxDepth_NeetCode(root.left), maxDepth_NeetCode(root.right))

'''
TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'
Reason: this is due to findHeight implicitly returning None when a return statement isn't specified
  - Notice in 4_BEST_Postorder_Traversal, we're not returning the function but rather the array from the function.
'''
def maxDepthV2(root):

    def findHeight(node):
        if not node:
            return 0
        findHeight(node.left) + 1
        findHeight(node.right) + 1
    
    return findHeight(root)