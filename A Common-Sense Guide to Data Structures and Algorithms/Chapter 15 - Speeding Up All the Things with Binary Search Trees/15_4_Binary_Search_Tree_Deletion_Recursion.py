class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.value = val
    self.leftChild = left
    self.rightChild = right

def delete(valueToDelete, node):
  # Base Case: Bottom of tree with parent node with no children
  if node is None:
    return None

  # Next two elif statements is trying to find the node we want to delete
  elif valueToDelete < node.value:
    node.leftChild = delete(valueToDelete, node.leftChild)
    return node
  
  elif valueToDelete > node.value:
    node.rightChild = delete(valueToDelete, node.rightChild)
    return node
  
  # If the current node is the one we want to delete
  elif valueToDelete == node.value:
    # Scenario 1: No left child and delete by returning its right child and subtree if exist to be its parent's new subtree
    if node.leftChild is None:
      return node.rightChild # Ends up being None anyways if rightChild doesn't exist
    
    # Scenario 2: No right child and delete by returning its left child and subtree if exist
    elif node.rightChild is None:
      return node.leftChild
    
    # Scenario 3: Two children - call lift function to change current node's value to value of its successor node
    else:
      node.rightChild = lift(node.rightChild, node)
      return node

# Helper function of finding successor node after the first right child by going to all subsequent left children
def lift(node, nodeToDelete):
  # Continue down the left node until there isn't any more left children node
  if node.leftChild:
    node.leftChild = lift(node.leftChild, nodeToDelete)
    return node
  # Once we reach our successor, we save that node's value to delete
  else:
    nodeToDelete.value = node.value
    return node.rightChild