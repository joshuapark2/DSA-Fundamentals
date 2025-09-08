def reorderList(head):
  """
  Do not return anything, modify head in-place instead.
  """
  slow, fast = head, head.next

  # Halves = +1/+2
  while fast and fast.next:
      slow = slow.next
      fast = fast.next.next
  
  half = slow.next # Current 2nd half
  slow.next = None # Break 1st half
  newHalf = None   # New 2nd half

  while half:
      increment = half.next
      half.next = newHalf
      newHalf = half
      half = increment
  
  f, b = head, newHalf
  while b:
      ftemp, btemp = f.next, b.next
      f.next = b
      b.next = ftemp
      f, b = ftemp, btemp