from LinkedList import LinkedList

ll = LinkedList()
ll.insertHead(2)
ll.insertHead(1)
ll.append(3)
ll.remove(2)
print(ll.toString())
print(f"链表的长度是：{ll.length()}")