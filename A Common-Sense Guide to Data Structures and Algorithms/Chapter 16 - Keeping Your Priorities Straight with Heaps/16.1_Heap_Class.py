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

'''
short-hand:
    def root_node(self):
        return self.data[0] if self.data else None
short-hand: 
    def last_node(self):
        return self.data[-1] if self.data else None

if self.data is not None -> will always be true since self.data will always be a list
if self.data: -> Checks for non-empty
'''