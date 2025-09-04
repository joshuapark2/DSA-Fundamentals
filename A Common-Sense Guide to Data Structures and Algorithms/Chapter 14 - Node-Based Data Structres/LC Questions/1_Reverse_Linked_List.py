class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head: ListNode):
  current = head
  prev = None

  while current:
      next_node = current.next
      current.next = prev
      prev = current
      current = next_node
  return prev


ll1 = ListNode([0, 1, 2, 3])
print(reverseList(ll1))



'''
# V2
    # Fix 1: Solve infinite loop by removing the if conditional. For LL we actually want a None value eventually to signal the end of our LL
    # Fix 1.1: You can remove next_node = None since we can still declare variables within a loop
    # Fix 1.2: You can squish current and prev into one line, like l, r = 0, len(newList) - 1, but the difference is negliable

    # Problem 1: Infinite Loop

def reverseList(head: ListNode):
  current = head
  prev = None
  next_node = None

  while current:
      if current.next:
          next_node = current.next
      current.next = prev
      prev = current
      current = next_node
  return prev


# V1
  # Fix 1: prev = current.val is the source of AttributeError: 'int' object has no attribute 'next'
  # Fix 2: Removing all ans.append and val is a step in the right direction due to explaination of problem 2

  # Problem 1: Somewhere in the loop I'm assigning current or (prev) to an int, leading to the error below
      AttributeError: 'int' object has no attribute 'next'
        if current.next:
  # Problem 2: You're treating a Linked List as a List, remember that we can only begin iteration at the 
      beginning of a list from the head. Adding ans = [] doesn't make sense since we can just return the tail
      to get the reverse order while preserving the data structure.
  

def reverseList(head: ListNode):
    current = head
    ans = []
    prev = None
    next_node = None

    while current:
        if current.val:
            next_node = current.next
        current.next = prev
        ans.append(current.val)
        prev = current.val
        current = next_node
    return ans
'''