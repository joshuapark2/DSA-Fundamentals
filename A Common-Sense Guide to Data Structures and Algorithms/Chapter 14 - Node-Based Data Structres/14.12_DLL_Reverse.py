class Node:
    def __init__(self, data):
        self.next_node = None
        self.previous_node = None
        self.data = data

class DoublyLinkedList:
    def __init__(self, first_node=None, last_node=None):
        self.first_node = first_node
        self.last_node = last_node

    def insert_at_end(self, value):
        new_node = Node(value)
        if self.first_node is None:
            self.first_node = new_node
            self.last_node = new_node
        else:
            new_node.previous_node = self.last_node
            self.last_node.next_node = new_node
            self.last_node = new_node

    def reverse_order(self):
        current = self.first_node
        self.last_node = current  # old head will become the tail

        prev_node = None
        while current is not None:
            # Swap next and previous pointers
            next_node = current.next_node
            current.next_node = prev_node
            current.previous_node = next_node

            # Move forward in the original order
            prev_node = current
            current = next_node

        # prev_node is now the new head
        self.first_node = prev_node

# Create an empty Doubly Linked List
dll = DoublyLinkedList()

# Insert nodes at the end
dll.insert_at_end("once")
dll.insert_at_end("upon")
dll.insert_at_end("a")
dll.insert_at_end("time")

dll.reverse_order()