class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None
        self.previous_node = None


class DoublyLinkedList:
    def __init__(self, first_node=None, last_node=None):
        self.first_node = first_node
        self.last_node = last_node

    def insert_at_end(self, value):
        new_node = Node(value)

        # If there are no elements in the linked list
        if self.first_node is None:
            self.first_node = new_node
            self.last_node = new_node
        else:
            # Link the new node to the current last node
            new_node.previous_node = self.last_node
            self.last_node.next_node = new_node

            # Update the last node reference
            self.last_node = new_node