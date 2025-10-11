class Stack:
    def __init__(self):
        self.list = []

    def isEmpty(self):
        return self.list == []

    def push(self, value):
        self.list.append(value)

    def pop(self):
        if(self.isEmpty()):
            print("Can't pop from empty stack")
            raise IndexError("pop from empty stack")
        return self.list.pop()

    def peek(self):
        if(self.isEmpty()):
            print("Can't peek from empty stack")
            raise IndexError("pop from empty stack")
        return self.list[-1]

    def size(self):
        return len(self.list)

    def clear(self):
        self.list.clear()

    def toString(self):
        return " ".join(str(x) for x in self.list)

