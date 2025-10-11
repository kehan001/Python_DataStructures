from Queue import Queue

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.dequeue()
print(q.toString())
print(q.size())