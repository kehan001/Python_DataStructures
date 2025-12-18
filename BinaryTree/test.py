from BinaryTree.TreeNode import TreeNode

array = "ABDH#K###E##CFI###G#J##"

#建造树，接收前序遍历数组
def createTree(array: str):
    #创建迭代器，方便遍历
    it = iter(array)

    def build():
        ch = next(it, None)
        if(ch == "#"):
            return
        node = TreeNode(ch)
        node.leftNode = build()
        node.rightNode = build()
        return node

    return build()

head = createTree(array)

#前序遍历
def preOrder(head):
    if(head is None):
        return
    print(head.data, end="")
    preOrder(head.leftNode)
    preOrder(head.rightNode)

preOrder(head)
print()


#中序遍历: 找完左子节点再输出
def inOrder(head):
    if(head is None):
        return
    inOrder(head.leftNode)
    print(head.data, end="")
    inOrder(head.rightNode)
inOrder(head)
print()

#后序遍历：左右子节点都找完了再输出
def postOrder(head):
    if(head is None):
        return
    postOrder(head.leftNode)
    postOrder(head.rightNode)
    print(head.data, end="")
postOrder(head)








        