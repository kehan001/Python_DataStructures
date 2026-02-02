#二叉排序树
from BinarySearchTree.treeNode import treeNode

treeArr = [70, 55, 49, 30, -1, 39, -1, -1, 53, -1, -1, -1, 80, 75, -1, -1, 98, 95, -1, -1, -1]

#建树
def createTree(treeArr):
    it = iter(treeArr)
    def build():
        curr = next(it, None)
        if curr == -1:
            return
        node = treeNode(curr)
        node.left = build()
        node.right = build()
        return node
    return build()

head = createTree(treeArr)

#前序遍历检查
def preOrder(head):
    if head is None:
        return
    print(head.data, end=" ")
    preOrder(head.left)
    preOrder(head.right)

preOrder(head)

#查找
def search(head, value):
    parent = None
    curr = head
    while curr:
        if curr.data == value:
            return curr, parent
        parent = curr
        if curr.data > value:
            curr = curr.left
        elif curr.data < value:
            curr = curr.right
    return None, parent

root, parent = search(head, 80)
print(f"\n{root.data if root else None}, {parent.data if parent else None}")

def insert(head, value):
    curr, parent = search(head, value)
    #如果未找到则创建新节点
    if curr == None:
        newNode = treeNode(value)
        if head is None:
            head = newNode
            return head
        if parent.data > value:
            parent.left = newNode
            return head
        elif parent.data < value:
            parent.right = newNode
            return head
    return head

head = insert(head, 99)
preOrder(head)

#删除操作
def deleteNode(node):
    if node.right is None: #无右子节点或无叶子节点
        return node.left
    elif node.left is None: #无左子节点
        return node.right
    else: #都有的话找左子树的最大值
        temp = node
        leftNode = node.left
        rightNode = node.right
        target = node.left
        while target.right:
            temp = target
            target = target.right
        if temp != node:
            temp.right = target.left
            target.left = leftNode
            target.right = rightNode
        else:
            target.right = rightNode
        return target

def delete(node, value):
    if node is None:
        print("Not found")
        return None
    else:
        if node.data == value:
            node = deleteNode(node)
        elif node.data > value:
            node.left = delete(node.left, value)
        elif node.data < value:
            node.right = delete(node.right, value)
    return node

head = delete(head, 80)
print()
preOrder(head)



