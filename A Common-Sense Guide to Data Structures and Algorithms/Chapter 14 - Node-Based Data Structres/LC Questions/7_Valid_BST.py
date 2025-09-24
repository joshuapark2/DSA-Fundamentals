'''
You're given a basic Binary Search Tree and the goal is to figure out if the given BST follows
all the properties of a BST. Return a boolean value
'''
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def isValidBST(root):
  return valid(root, float('-inf'), float('inf'))

def valid(node, lower, upper):
  if not node:
    return True
  elif not (lower < node.val and node.val < upper):
    return False
  else:
    return (valid(node.left, lower, node.val) and valid(node.right, node.val, upper))