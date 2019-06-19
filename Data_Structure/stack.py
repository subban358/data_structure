class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)				

    def pop(self):

        if self.is_empty():
            print("No elements present !!")
        else:
            return self.items.pop()
    
    def is_empty(self):
        return self.items == []
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        
    def get_stack(self):
        return self.items

s=Stack()


s.pop()
print(s.get_stack())        

