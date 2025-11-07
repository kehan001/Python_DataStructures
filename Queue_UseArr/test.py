#循环列表懒得写了，就多以下几点
"""
1. 队尾指针rear = (rear+1) % MAXSIZE 指向当前元素应存入的位置
2. 对头指针front = (front+1) % MAXSIZE 指向应取出的位置
2. 判满：(rear+1) % MAXSIZE == front
    注意：循环队列实际存储元素永远比MAXSIZE小一
    ex:MAXSIZE=5, rear=4, front=1 按道理4这个位置还可以添加元素，但是根据公式链表已满
3. 判空：rear == front
"""
from Queue import Queue

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.dequeue()
print(q.toString())
print(q.size())