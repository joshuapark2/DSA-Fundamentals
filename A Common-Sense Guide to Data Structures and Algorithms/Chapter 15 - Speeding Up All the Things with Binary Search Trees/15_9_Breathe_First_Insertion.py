from collections import deque
'''
Level-Order Insertion (Breathe-First Construction)
deque: Double-Ended-Queue (Append and Pop both left and right)
  - Building from Breathe-First, we want to process via First-In, Last-Out (FILO)
  - Note that Deque can be BOTH Stack and Queue depending on use case (reason it's called Double-Ended Queue)
  - .append() / .pop() -> Stack behavior (right side)
  - .appendleft() / .popleft() -> Queue behavior (left side)
'''

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def print_tree(node, level=0, prefix="Root: "):
    if node:
        print("    " * level + prefix + str(node.val))
        if node.left or node.right:
            print_tree(node.left, level + 1, "L--- ")
            print_tree(node.right, level + 1, "R--- ")

def build_tree(array):
  if not array or array[0] is None:
    return None

  # Basically have an special type of array called queue
  # Within our queue, we have 
  root = TreeNode(array[0])
  queue = deque([root])
  i = 1

  while queue and i < len(array):
    current = queue.popleft()

    # Left Child
    if i < len(array) and array[i] is not None:
      current.left = TreeNode(array[i])
      queue.append(current.left)
    i += 1

    # Right Child
    if i < len(array) and array[i] is not None:
      current.right = TreeNode(array[i])
      queue.append(current.right)
    i += 1
  
  return root

root = build_tree([3, 9, 20, None, None, 15, 7])
print_tree(root)