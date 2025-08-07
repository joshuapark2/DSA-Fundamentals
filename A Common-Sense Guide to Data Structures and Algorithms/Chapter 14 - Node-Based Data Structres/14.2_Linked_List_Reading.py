class Node:
    def __init__(self, data):
        # Creating our two cells per node (data, address)
        self.data = data
        self.next_node = None

class LinkedList:
    def __init__(self, first_node):
        self.first_node = first_node

    def read(self, index):
        current_node = self.first_node
        current_index = 0

        while current_index < index:
            if current_node is None:
                return Node # We've go past the tail

            current_node = current_node.next_node
            current_index += 1

        if current_node is None:
            return None # Index Out of Bounds

        return current_node.data

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

# Read data by index
print(linked_list.read(0))  # Output: once
print(linked_list.read(2))  # Output: a
print(linked_list.read(5))  # Output: None (out of bounds)
