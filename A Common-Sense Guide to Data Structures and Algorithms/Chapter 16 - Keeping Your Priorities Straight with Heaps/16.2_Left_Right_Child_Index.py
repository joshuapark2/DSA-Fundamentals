class Heap:
    def __init__(self):
        self.data = []

    def root_node(self):
        if self.data:  # checks for non-empty
            return self.data[0]
        else:
            return None
        
    def last_node(self):
        if self.data:  # checks for non-empty
            return self.data[-1]
        else:
            return None
    
    def left_child_index(self, index):
        return (index * 2) + 1

    def right_child_index(self, index):
        return (index * 2) + 2
    
    def parent_index(self, index):
        return (index - 1) // 2
    