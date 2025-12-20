#以最常用的中序遍历为例子
from Threaded_BinaryTree.TreeNode import TreeNode

array = "ABDH#K###E##CFI###G#J##"

#前序建普通树
def createTree(array: str):
    it = iter(array)

    def build():
        data = next(it, None)
        if(data == "#"):
            return
        node = TreeNode(data)
        node.leftNode = build()
        node.rightNode = build()
        return node

    return build()

#将树线索化
def inOrderThreading(T):
    #创建头节点，用于链接链表和作为结束标志
    global head
    head = TreeNode()
    head.rtag = 1
    head.leftNode = T #左边链接root节点, ltag依旧为0
    head.rightNode = head #链接自己的目的是通过threading的第一轮递归

    global prev#记录上一个访问的值，用于确定最后一个节点
    prev = head
    threading(T) #给每个节点添加线索
    prev.rightNode = head
    prev.rtag = 1
    head.rightNode = prev

    return head


#线索化
def threading(T):
    global prev
    if(T != None):
        threading(T.leftNode)
        if(T.leftNode == None):
            T.ltag = 1
            T.leftNode = prev
        if(prev.rightNode == None):
            prev.rtag = 1
            prev.rightNode = T
        prev = T
        threading(T.rightNode)

#遍历
def inOrder(T):
    curr = T.leftNode
    while(curr != head):
        while(curr.ltag == 0):
            curr = curr.leftNode
        print(curr.data, end="")
        while(curr.rtag == 1 and curr.rightNode != T):
            curr = curr.rightNode
            print(curr.data, end="")
        curr = curr.rightNode

root = createTree(array)
head = inOrderThreading(root)
inOrder(head)




