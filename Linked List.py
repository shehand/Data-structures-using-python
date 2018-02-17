class Node:

    def __init__(self,data=None,next = None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)

node1 = Node("Car")
node2 = Node("Bus")
node3 = Node("Lorry")
node1.next = node2
node2.next = node3
node3.next = None

def PrintList(node):
    while node != None:
        print(node)
        node = node.next
    print()
PrintList(node1)
PrintList(node3)

def printBackward(lis):
    if lis == None:return
    head = lis
    tail = lis.next
    printBackward(tail)
    print(head)

head = lis
tail = lis.next
def printBackward(list):
    if lis == None:return
    printBackward(list.next)
    print(head)
        
def RemoveNode(list):
    if lis ==  None:return
    first = lis
    second = lis.next
    first.next = second.next
    second.next = None
    return second
