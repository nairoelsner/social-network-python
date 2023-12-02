class Node:
    def __init__(self, value, nextNode = None):
        self.value = value
        self.nextNode = nextNode

class LinkedQueue:
    def __init__(self):
        self.start = None
        self.end = None
        self.length = 0

    def enqueue(self, value):
        new_node = Node(value)
        if self.start == None:
            self.start = new_node
            self.end = new_node
        else:
            self.end.nextNode = new_node
            self.end = new_node

        self.length += 1
        return True

    def dequeue(self):
        if self.start == None:
            return False
        value = self.start.value
        self.start = self.start.nextNode
        self.length -= 1
        return value

    def read(self):
        if self.start == None:
            return False
        
        return self.start.value
    
    def destroy(self):
        while self.start != None:
            self.delete()