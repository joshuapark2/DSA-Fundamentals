class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.value = val
    self.leftChild = left
    self.rightChild = right
  

def search(searchValue, node):
  # Base Case: Nonexistent or found value
  if node is None or node.value == searchValue:
    return node

  # Search left if value is less than searchValue
  elif searchValue < node.value:
    return search(searchValue, node.leftChild)

  # Search right if value is greater than search Value
  else:
    return search(searchValue, node.rightChild)

def insert(value, node):
  if value < node.value:
    # Edge case of left child not existing, add value as left child
    if node.leftChild is None:
      node.leftChild = TreeNode(value)
    else:
      insert(value, node.leftChild)

  elif value > node.value:
    # If right child doesn't exist, add value as right child
    if node.rightChild is None:
      node.rightChild = TreeNode(value)
    else:
      insert(value, node.rightChild)



node1 = TreeNode(25)
node2 = TreeNode(75)
root = TreeNode(50, node1, node2)