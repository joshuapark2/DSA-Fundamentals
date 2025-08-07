class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None

class LinkedList:
    def __init__(self, first_node):
        self.first_node = first_node

    def insert_at_index(self, index, value):
        new_node = Node(value)

        # If inserting at the beginning
        if index == 0:
            new_node.next_node = self.first_node
            self.first_node = new_node
            return

        # Inserting at any other position
        current_node = self.first_node
        current_index = 0

        # Traverse to the node before the insertion point
        while current_index < index - 1:
            if current_node is None:
                raise IndexError("Index out of bounds")
            current_node = current_node.next_node
            current_index += 1

        new_node.next_node = current_node.next_node
        current_node.next_node = new_node

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

print(linked_list.insert_at_index(2, 'yay')) # 'yay'
