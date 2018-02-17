class Queue:
    def __init__(self):
        self.items = []

    def __repr__(self):
        return repr(self.items)

    def enqueue(self,v):
        self.items.append(v)

    def dequeue(self):
        return self.items.pop(0)

    def isEmpty(self):
        print (len(self.items)==0)

    def size(self):
        return len(self.items)

    def top(self):
        return self.items[0]

