class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = Node

class LinkedList:
    def __init__(self, first_node):
        self.first_node = first_node

# Create the nodes
node_1 = Node('once')
node_2 = Node('upon')
node_3 = Node('a')
node_4 = Node('time')

# Link the Nodes
node_1.next_node = node_2
node_2.next_node = node_3
node_3.next_node = node_4

# Create linked list
linked_list = LinkedList(node_1)

# Access first node's data
print(linked_list.first_node.data)  # Output: once