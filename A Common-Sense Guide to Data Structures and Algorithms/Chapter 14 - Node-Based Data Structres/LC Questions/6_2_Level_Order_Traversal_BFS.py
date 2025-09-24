'''
You're given an array as a pseudo-tree where each element is a TreeNode with val, left and right
The goal is to seperate each level so that we have [[level1], [level2], [level3]]
'''
from collections import deque

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def breathe_first_search(root):
  deque = deque()
  deque.append(root)
  main = []

  while deque:
    sub = []
    for i in range(len(deque)):
      node = deque.popleft()
      if node:
        sub.append(node.val)
        deque.append(node.left)
        deque.append(node.right)
    if sub:
      main.append(sub)
    
  return main
