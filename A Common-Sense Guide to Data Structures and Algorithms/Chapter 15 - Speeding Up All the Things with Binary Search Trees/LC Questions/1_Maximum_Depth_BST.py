'''
A binary tree's maximum depth is the number of nodes along the longest path from 
  the root node down to the farthest leaf node.
'''
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

  def __repr__(self):
    return f"TreeNode(val={self.val}, left={self.left}, right={self.right})"

def maxDepth(root):
  if not root:
    return 0

  return 1 + max(maxDepth(root.left), maxDepth(root.right))