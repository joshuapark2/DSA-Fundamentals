class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def create_linked_list(array):
    dummy = Node()
    current = dummy

    for v in array:
        current.next = Node(v)
        current = current.next

    return dummy.next

def print_linked_list(linked_list: Node):
    current = linked_list

    while current:
        print(current.val, end = " -> ")
        current = current.next

l1 = create_linked_list([1, 2, 3, 4])
print_linked_list(l1)

'''
Explanation:
  - We can't print out a linked list in one go because they're different from lists where each node has its own
    value and address. We are able to link them together from one to another like playing telephone, but they
    can't exact with anyone besides those who are next to them.

Summary of Mistakes:
    current.next = Node(v) is important because is this how we preserve the link. Simply doing current = Node(v)
    would be the same as creating a node in space and isolation. Also current.next and dummy.next are both
    used to keep the code cleaner by avoiding indexing via `head = Node(array[0])`, then having to do 
    `for v in array[1:]`
'''