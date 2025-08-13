class Node:
  def __init__(self, data):
    self.data = data
    self.next_node = None
    self.previous_node = None
  
class DoublyLinkedList:
  def __init__(self, first_node=None, last_node=None):
    self.first_node = first_node
    self.last_node = last_node