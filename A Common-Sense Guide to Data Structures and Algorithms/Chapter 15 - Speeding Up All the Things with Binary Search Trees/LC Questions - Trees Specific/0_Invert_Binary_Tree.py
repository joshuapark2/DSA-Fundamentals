'''
Invert a Binary Tree is the same as asking to mirror:
  - The algorithm is very simple when you realize that you're just swapping the left and right subtree under the current root
  - Confusion occurred when think that you're swapping the furthest and lowest left subchild with the furhest and lowest right child
    When in reality, that happens from the top down when mirroring. This gets rid of the confusion of having to use pointers
    and simply use variable temp followed by postorder traversal (left, right current)

https://www.geeksforgeeks.org/dsa/write-an-efficient-c-function-to-convert-a-tree-into-its-mirror-tree/
'''

class TreeNode:
  def __init__(self, val = 0, left= None, right= None):
    self.val = val
    self.left = left
    self.right = right


def invertTree(root):
  if not root:
    return None

  temp = root.left
  root.left = root.right
  root.right = temp

  invertTree(root.left)
  invertTree(root.right)

  return root