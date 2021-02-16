class Stack:
    def __init__(self):
        self.items=[]
    def push(self,item):
        self.items.append(item)
        return self
    
stack = Stack()

stack.push(5)
stack.push(6)
stack.push(8)

print(stack.items)



    
    