class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None

class LinkedList:
    def __init__(self, first_node):
        self.first_node = first_node

    def index_of(self, value):
        current_node = self.first_node
        current_index = 0

        while current_node is not None:
            if current_node.data == value:
                return current_index
            current_node = current_node.next_node
            current_index += 1

        return None

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

# Search for value's index
print(linked_list.index_of('time')) # 3
print(linked_list.index_of('upon')) # 1
print(linked_list.index_of('never')) # None