class Queue:
    def __init__(self):
        self.data = []

    def enqueue(self, element):
        self.data.append(element)

    def dequeue(self):
        # Remove and return the first element (like Ruby's shift)
        return self.data.pop(0) if self.data else None

    def read(self):
        # Return the first element without removing it
        return self.data[0] if self.data else None
