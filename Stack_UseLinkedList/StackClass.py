from Node import Node

class Stack:
    def __init__(self):
        self.top = None #栈顶指针

    def isEmpty(self):
        return self.top is None

    def push(self, data):
        newNode = Node(data)
        newNode.next = self.top
        self.top = newNode

    def pop(self):
        if (self.top.next is None):
            print("Stack is empty")
            raise IndexError("Stack is empty")
        data = self.top.data
        self.top = self.top.next
        return data

    def peek(self):
        if(self.isEmpty()):
            print("Empty Stack")
        return self.top.data

    def size(self):
        count = 0
        curr = self.top
        while (curr):
            count += 1
            curr = curr.next
        return count