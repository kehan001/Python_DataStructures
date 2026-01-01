from LevelOrderTraversal.TreeNode import TreeNode

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

#层序遍历，深度
def levelOrder(root: TreeNode):
    if root is None:
        return

    queue = []
    queue.append(root)
    count = 0
    while(queue): #队列不为空时执行
        levelSize = len(queue) #每层的节点数，用于判断层数什么时候加
        count += 1
        for i in range(levelSize): #遍历当前层的节点
            curr = queue.pop(0) #输出，出队
            print(curr.data, end="")
            for i in curr.children: #子节点入队
                queue.append(i)
    return count

print(f"\n{levelOrder(A)}")
