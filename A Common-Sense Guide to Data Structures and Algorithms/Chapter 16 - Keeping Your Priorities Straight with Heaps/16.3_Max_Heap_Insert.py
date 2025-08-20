class MaxHeap:
  def __init__(self):
    self.data = []
  
  def parent_index(self, index):
    return (index - 1) // 2

  def insert(self, value):
    # Insert value at the end of the heap
    self.data.append(value)

    # Index of the newly inserted node
    new_node_index = len(self.data) - 1

    # Trickle up
    while new_node_index > 0 and self.data[new_node_index] > self.data[self.parent_index(new_node_index)]:
      # Swap with parent
      parent_idx = self.parent_index(new_node_index)
      self.data[parent_idx], self.data[new_node_index] = self.data[new_node_index], self.data[parent_idx]

      # Move up
      new_node_index = parent_idx

# heap = MaxHeap()
# heap.insert(10)
# heap.insert(20)
# heap.insert(5)


heap = MaxHeap()
for n in [10,9, 8, 6, 5, 7, 4, 2, 1, 3]:
    heap.data.append(n)
heap.insert(11)
print(heap.data) # [20, 10, 5]