class Node:
    def __init__(self, data):
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

    def index_of(self, value):
        current_node = self.first_node
        current_index = 0

        while current_node is not None:
            if current_node.data == value:
                return current_index
            current_node = current_node.next_node
            current_index += 1

        return None

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

# Read data by index
print(linked_list.read(0))
print(linked_list.read(2))
print(linked_list.read(5))

# Search for value's index
print(linked_list.index_of('time')) # 3
print(linked_list.index_of('upon')) # 1
print(linked_list.index_of('never')) # None

# Insert at index
print(linked_list.insert_at_index(2, 'yay'))
print(linked_list.read(2)) # 'yay'

# Delete at index
print(linked_list.delete_at_index(2))
print(linked_list.read(2)) # a