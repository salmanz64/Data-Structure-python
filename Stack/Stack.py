class Stack:
    def __init__(self):
        self.items= []
        
    def isEmpty(self):
        return self.items == []
    
    def size(self):
        return len(self.items)
    
    def peek(self):
        return self.items[-1]
        
    def push(self,item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    
# s=Stack()

# print(s.isEmpty())
# s.push(4)
# s.push('dog')
# print(s.peek())
# s.push(True)
# print(s.size())
# print(s.isEmpty())
# s.push(8.4)
# print(s.pop())
# print(s.pop())
# print(s.size())
