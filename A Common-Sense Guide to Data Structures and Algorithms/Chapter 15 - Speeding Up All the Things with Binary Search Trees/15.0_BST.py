class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right
  
  def __repr__(self):
    return f"TreeNode({self.val}, left={self.left}, right={self.right})"

def insert(new_node, curr_node):
  # insert to the left
  if new_node <= curr_node.val:
    if not curr_node.left:
      curr_node.left = TreeNode(new_node)
    else:
      insert(new_node, curr_node.left)

  # insert to the right
  elif new_node > curr_node.val:
    if not curr_node.right:
      curr_node.right = TreeNode(new_node)
    else:
      insert(new_node, curr_node.right)

node1 = TreeNode(25)
node2 = TreeNode(75)
root = TreeNode(50, node1, node2)

print(root)
