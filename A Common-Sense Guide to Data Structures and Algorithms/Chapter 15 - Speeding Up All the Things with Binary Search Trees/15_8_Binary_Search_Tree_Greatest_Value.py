class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.value = val
    self.leftChild = left
    self.rightChild = right

def max(node):
  if node.rightChild:
    max(node.rightChild)
  else:
    print(node.value)
    return node.value

node1 = TreeNode(25)
node2 = TreeNode(75)
root = TreeNode(50, node1, node2)
max(root)