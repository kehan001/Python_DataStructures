from Node import Node

class LinkedList:
    #构造方法，即创建头节点
    def __init__(self):
        self.head = Node(None)

    #头节点插入
    def insertHead(self, data):
        newNode = Node(data) #创建节点对象
        newNode.next = self.head.next #把头结点下一个节点的地址值赋值给当前节点的next
        self.head.next = newNode #把当前节点的地址值赋值给头节点的next

    #遍历链表
    def toString(self):
        list = []
        cur = self.head.next
        while (cur):
            list.append(str(cur.data))
            cur = cur.next
        return "->".join(list)

    #获取尾节点
    def getTail(self) -> Node:
        cur = self.head.next
        while (cur.next):
            cur = cur.next
        return cur

    #尾插法
    def append (self, data):
        newNode = Node(data)
        if (self.head.next is None):
            self.head.next = newNode
        else:
            tailNode = self.getTail()
            tailNode.next = newNode #把当前节点的地址赋值给尾节点的next

    #插入节点
    def insert(self, pos, data):
        if(pos < 0): #判断插入位置是否为负数
            print("This position is not available")
            raise IndexError("Position cannot be negative")

        newNode = Node(data)
        prev = self.head #插入位置前一个节点
        curr = 0 #当前遍历到的索引

        while(prev and curr < pos): #遍历到插入位置的前一个节点
            prev = prev.next
            curr += 1

        newNode.next = prev.next #插入
        prev.next = newNode

    #删除节点
    def remove(self, pos):
        if(pos < 0):
            print("This position is not available")
            raise IndexError("Position cannot be negative")

        prev = self.head
        curr = 0

        while(prev.next and curr < pos):
            prev = prev.next
            curr += 1

        if(prev is None):
            raise IndexError("Index out of bounds")

        deleteNode = prev.next #要删除的节点
        prev.next = deleteNode.next #更改前一个节点存储的地址
        deleteNode.next = None #断开被删除的节点的链接

    #获取链表长度
    def length(self):
        length = 0
        curr = self.head

        while(curr.next):
            curr = curr.next
            length += 1

        return length

    #释放链表(Python不需要，仅仅作为练习)
    def clear(self):
        curr = self.head.next  #记录当前节点

        while(curr): #判断当前节点是否为None
            nextNode = curr.next #把当前节点的下一个节点的地址赋值给一个变量
            curr = None #free(), Python无这个方法所以只是意思一下
            curr = nextNode #指针重新指向下一个节点

        self.head.next = None #释放头节点的资源

    #反转链表
    def reverse(self):
        first = None #指针1
        second = self.head.next #指针2
        while(second):
            third = second.next #指针3
            second.next = first #把节点的next换位它的前一个节点
            first = second
            second = third
        self.head.next = first
        return self






