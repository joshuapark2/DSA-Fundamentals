# Node for Doubly Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None
        self.previous_node = None


# Doubly Linked List
class DoublyLinkedList:
    def __init__(self, first_node=None, last_node=None):
        self.first_node = first_node
        self.last_node = last_node

    def insert_at_end(self, value):
        new_node = Node(value)
        # If the list is empty
        if self.first_node is None:
            self.first_node = new_node
            self.last_node = new_node
        else:
            # Link the new node
            new_node.previous_node = self.last_node
            self.last_node.next_node = new_node
            # Update last_node
            self.last_node = new_node

    def remove_from_front(self):
        if self.first_node is None:
            return None
        removed_node = self.first_node
        self.first_node = self.first_node.next_node
        if self.first_node:
            self.first_node.previous_node = None
        else:
            # List became empty
            self.last_node = None
        return removed_node


# Queue implemented using Doubly Linked List
class Queue:
    def __init__(self):
        self.data = DoublyLinkedList()

    def enqueue(self, element):
        self.data.insert_at_end(element)

    def dequeue(self):
        removed_node = self.data.remove_from_front()
        return removed_node.data if removed_node else None

    def read(self):
        return self.data.first_node.data if self.data.first_node else None


# Example usage:
q = Queue()
q.enqueue("A")
q.enqueue("B")
q.enqueue("C")

print(q.read())     # Output: A
print(q.dequeue())  # Output: A
print(q.read())     # Output: B
