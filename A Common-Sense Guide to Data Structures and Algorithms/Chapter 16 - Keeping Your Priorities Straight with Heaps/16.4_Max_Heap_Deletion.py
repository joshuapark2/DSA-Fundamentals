class MaxHeap:
  def __init__(self):
    self.data = []

  def root_node(self):
    return self.data[0] if self.data else None
  
  def last_node(self):
    return self.data[-1] if self.data else None
  
  def left_child_index(self, index):
    return (index * 2) + 1
  
  def right_child_index(self, index):
    return (index * 2) + 2
  
  def parent_index(self, index):
    return (index - 1) // 2
  
  def has_greater_child(self, index):
    left = self.left_child_index(index)
    right = self.right_child_index(index)

    # Check if left child exists and is greater
    if left < len(self.data) and self.data[left] > self.data[index]:
      return True
    
    # Check if right child exists and is greater
    if right < len(self.data) and self.data[right] > self.data[index]:
      return True
    
    return False
  
  def calculate_larger_child_index(self, index):
    left = self.left_child_index(index)
    right = self.right_child_index(index)

    # If no right child, return left
    if right >= len(self.data):
      return left
    
    # If right > left, return right:
    if self.data[right] > self.data[left]:
      return right
    else:
      return left
    
  def delete(self):
    if not self.data:
      return None
    
    if len(self.data) == 1:
      return self.data.pop()
    
    # Replace root with last node
    root_value = self.data[0]
    self.data[0] = self.data.pop()

    trickle_node_index = 0

    # Trickle down
    while self.has_greater_child(trickle_node_index):
      larger_child_index = self.calculate_larger_child_index(trickle_node_index)

      # Swap
      self.data[trickle_node_index], self.data[larger_child_index] = self.data[larger_child_index], self.data[trickle_node_index]

      # Move down
      trickle_node_index = larger_child_index

    return root_value

heap = MaxHeap()
for n in [50, 30, 20, 15, 10, 8, 16]:
    heap.data.append(n)  # skipping insert for brevity

print(heap.data)   # [50, 30, 20, 15, 10, 8, 16]
print(heap.delete())  # 50 (root removed)
print(heap.data)   # [30, 16, 20, 15, 10, 8]