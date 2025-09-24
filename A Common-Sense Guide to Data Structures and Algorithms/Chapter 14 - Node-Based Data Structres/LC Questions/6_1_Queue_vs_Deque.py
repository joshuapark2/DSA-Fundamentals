import queue
from collections import deque

### Queue ###
new_queue = queue.Queue()

new_queue.put('item1')
new_queue.put('item2')

print(new_queue) # <queue.Queue object at 0x10465a8d0>
print(new_queue.qsize()) # 2

first_item = new_queue.get() # removes and return first into in queue FIFO
print(first_item) # 'item1'
print(new_queue.qsize()) #1

### Deque ### - Double-Ended Queue -> Adding and Removing from both sides
de = deque(['name', 'age', 'DOB'])
print(de) # deque(['name', 'age', 'DOB'])

de.append('gender') # Adds to the end/right side of the queue
print(de) # deque(['name', 'age', 'DOB', 'gender'])

de.appendleft('beginning')
print(de) # deque(['beginning', 'name', 'age', 'DOB', 'gender'])
de.pop() # Removes at the end like a stack - FILO
de.popleft() # Removes and supports FIFO
print(de) # deque(['name', 'age', 'DOB'])
