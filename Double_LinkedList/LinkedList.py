from Node import Node

class LinkedList:
    # 构造方法，即创建头节点
    def __init__(self):
        self.head = Node()

    #头插法
    def insertHead(self, data):
        newNode = Node(data)
        if (self.head.next is None): #判断头节点后面有没有其他节点
            self.head.next = newNode
        else:
            newNode.prev = self.head #把头节点赋值给当前节点的prev
            newNode.next = self.head.next #把头节点的下一个节点赋值给当前节点的next
            self.head.next.prev = newNode #把当前节点赋值给头结点的下一个节点的prev
            self.head.next = newNode #把当前节点赋值给头节点的next
            #最后两行的顺序不能乱

    #遍历链表，与单链表一样
    def toString(self):
        list = []
        cur = self.head.next
        while (cur):
            list.append(str(cur.data))
            cur = cur.next
        return " ".join(list)

    #尾插法, 和单链表的方法一样。只不过多了一个prev“指针”
    def append(self, data):
        newNode = Node(data)
        if(self.head.next is None):
            self.head.next = newNode
            newNode.prev = self.head
        else:
            tailNode = self.getTail()
            tailNode.next = newNode
            newNode.prev = tailNode


    #获取尾节点
    def getTail(self):
        curr = self.head.next
        while(curr.next):
            curr = curr.next
        return curr

    #获取链表长度
    def length(self):
        len = 0
        curr = self.head.next
        while(curr):
            curr = curr.next
            len += 1
        return len


    #插入数据，思路也和单链表相同
    def insert(self, pos, data):
        newNode = Node(data)
        curr = self.head
        if(pos > self.length() or pos < 0):
            print("Index out of range")
            raise IndexError("Index out of bounds")

        for i in range(pos):
            curr = curr.next

        newNode.prev = curr
        newNode.next = curr.next
        if(curr.next):
            curr.next.prev = newNode
        curr.next = newNode

    #删除节点, 这并不是真正意义的删除，只是作为练习
    def remove(self, pos):
        if(pos < 0 or pos >= self.length()):
            print("Index out of range")
            raise IndexError("Index out of bounds")

        first = self.head
        for i in range(pos):
            first = first.next


        second = first.next
        if(second.next):
            third = second.next
            third.prev = first
            first.next = third
        else:
            first.next = None
