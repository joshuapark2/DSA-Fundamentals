class Stack:
  def __init__(self):
    self.data = []
  
  def push(self, element):
    self.data.append(element)
  
  def pop(self):
    return self.data.pop() if self.data else None

  def read(self):
    return self.data[-1] if self.data else None


s = Stack()

s.push(10)
s.push(20)
print(s.read()) # 20
print(s.pop()) # 20
print(s.read()) # 20