class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None

class LinkedList:
    def __init__(self, first_node):
        self.first_node = first_node

    def delete_at_index(self, index):
        # If deleting the first node
        if index == 0:
            if self.first_node is not None:
                self.first_node = self.first_node.next_node
            return

        current_node = self.first_node
        current_index = 0

        # Traverse to the node before the one to delete
        while current_index < index - 1:
            if current_node is None or current_node.next_node is None:
                raise IndexError("Index Out of Bounds")
            current_node = current_node.next_node
            current_index += 1

        # Skip the node at the target index
        if current_node.next_node is not None:
            current_node.next_node = current_node.next_node.next_node
        else:
            raise IndexError("Index Out of Bounds")

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

# Delete at index
print(linked_list.delete_at_index(2)) # a