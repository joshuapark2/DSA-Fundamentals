class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.value = val
    self.leftChild = left
    self.rightChild = right

def traverse_and_print(node):
  if node is None:
    return
  traverse_and_print(node.leftChild)
  print(node.value)
  traverse_and_print(node.rightChild)