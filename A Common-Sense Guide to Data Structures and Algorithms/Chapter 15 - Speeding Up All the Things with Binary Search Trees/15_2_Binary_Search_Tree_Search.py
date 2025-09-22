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

node1 = TreeNode(25)
node2 = TreeNode(75)
root = TreeNode(50, node1, node2)
search(25, root) # 25