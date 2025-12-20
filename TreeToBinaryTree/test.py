from xml.dom.minicompat import defproperty

from TreeToBinaryTree.BinaryTreeNode import BinaryTreeNode
from TreeToBinaryTree.TreeNode import TreeNode

#构造树，A为根节点
A = TreeNode("A")
B = TreeNode("B")
C = TreeNode("C")
D = TreeNode("D")
E = TreeNode("E")
F = TreeNode("F")
G = TreeNode("G")
A.children = [B, C, D]
B.children = [E, F]
D.children = [G]

def tree_to_binary(node: TreeNode):
    if node is None:
        return
    bi_node= BinaryTreeNode(node.data) #创建二叉树的节点对象
    if not node.children: #没有子节点说明是叶子节点不用操作直接返回
        return bi_node
    firstChild = node.children[0] #第一个子节点挂到二叉树节点的right
    bi_node.leftChild = tree_to_binary(firstChild) #一条路走到头的左子节点全部连上

    prev = bi_node.leftChild #兄弟节点之间互相连接
    for i in node.children[1:]:
        current = tree_to_binary(i)
        prev.rightChild = current
        prev = current
    return bi_node

def preOrder(node: BinaryTreeNode):
    if node is None:
        return
    print(node.data, end="")
    preOrder(node.leftChild)
    preOrder(node.rightChild)

root = tree_to_binary(A)
preOrder(root)

