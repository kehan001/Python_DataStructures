from LinkedList import LinkedList
#修改数据多的情况用链表，读取数据多的用数组
l = LinkedList()
l.insertHead(2)
l.insertHead(1)
l.append(4)
l.insert(2, 3)
l.delete(1)
l.toString()
print(f"\n列表的长度是: {l.length()}")
l.clear()
print(l.toString())