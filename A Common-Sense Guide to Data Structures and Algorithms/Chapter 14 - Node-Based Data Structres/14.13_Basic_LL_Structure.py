class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

def linkedList(head: ListNode):
  current = head
  nodes = []

  while current:
    nodes.append(current.val)
    current = current.next
  print(nodes)


ll1 = ListNode([0,1, 2, 3])
linkedList(ll1)