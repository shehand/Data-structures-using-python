class StackNode:
    def __init__(self,value,link):
        self.data = value
        self.next = link

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def isEmpty(self):
        return self.top == None

    def __len__(self):
        return self.size

    def peek(self):
        return self.top.data

    def push(self,value):
        node = StackNode(value,self.top)
        self.top = node
        self.size += 1

    def pop(self):
        if self.isEmpty():
            print ("can't pop from an empty stack")
        else:
            current = self.top
            if current.next == None:
                self.top = None
            else:
                self.top = current.next
            self.size -= 1
            return current.data
        
    
