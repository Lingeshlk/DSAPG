class stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)
s = stack()
s.push(5)
s.push(10)
print(s.pop())   # Output: 10
print(s.peek())  # Output: 5
print(s.size())