class Queue:
    def __init__(self):
        self.list = []

    def isEmpty(self):
        return len(self.list) == 0

    def enqueue(self, data):
        self.list.append(data)

    def dequeue(self):
        return self.list.pop(0)

    def size(self):
        if(self.isEmpty()):
            raise IndexError("Queue is empty")
        return len(self.list)

    def peek(self):
        if(self.isEmpty()):
            raise IndexError("Queue is empty")
        return self.list[0]

    def toString(self):
        return " ".join(str(i) for i in self.list)

