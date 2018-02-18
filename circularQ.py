
class Queue:

    def __init__(self, maxSize):
        self.front = 0
        self.maxSize = maxSize
        self.items = []
        self.back = maxSize - 1

    def enqueue(self, item):
        if self.isFull != True:
            self.back = (self.back + 1) % self.maxSize
            self.items.insert(self.back, item)
        else:
            return "Queue is already full"

    def dequeue(self):
        if self.isEmpty != True:
            print(self.items.pop(self.front))
            self.front = (self.front + 1) % self.maxSize
        else:
            return "Queue is empty"
    def isEmpty(self):
        return self.items == []

    def isFull(self):
        return len(self.items) == self.maxSize
        
