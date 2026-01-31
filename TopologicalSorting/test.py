from Stack_UseArr.StackClass import Stack
from TopologicalSorting.node import node
from TopologicalSorting.vertexNode import vertexNode

vertex = []
n = 14
edge = 20
for i in range(n):
    vertex.append(f"V{i}")

adj_digraph = []
for i in range(n):
    adj_digraph.append([])
    for j in range(n):
        adj_digraph[i].append(0)

adj_digraph[0][4] = 1
adj_digraph[0][5] = 1
adj_digraph[0][11] = 1
adj_digraph[1][2] = 1
adj_digraph[1][4] = 1
adj_digraph[1][8] = 1
adj_digraph[2][5] = 1
adj_digraph[2][6] = 1
adj_digraph[2][9] = 1
adj_digraph[3][2] = 1
adj_digraph[3][13] = 1
adj_digraph[4][7] = 1
adj_digraph[5][8] = 1
adj_digraph[5][12] = 1
adj_digraph[6][5] = 1
adj_digraph[8][7] = 1
adj_digraph[9][10] = 1
adj_digraph[9][11] = 1
adj_digraph[10][13] = 1
adj_digraph[12][9] = 1

#顶点对象集合
vnode = []
for i in range(n):
    vnode.append(vertexNode(i))
#邻接矩阵转邻接表
def to_adj_list(G):
    global vnode
    for i in range(n):
        for j in range(n):
            if G[i][j] == 1:
                newNode = node(j)
                newNode.next = vnode[i].next
                vnode[i].next = newNode
                vnode[j].entry += 1

def sort(vnode):
    result = []
    stack = Stack()
    for i in range(n):
        if vnode[i].entry == 0:
            stack.push(vnode[i])

    while not stack.isEmpty():
        curr = stack.pop()
        result.append(curr)
        e = curr.next
        while e:
            k = e.data
            vnode[k].entry -= 1
            if vnode[k].entry == 0:
                stack.push(vnode[k])
            e = e.next
    return " -> ".join(vertex[i.data] for i in result)

to_adj_list(adj_digraph)
print(sort(vnode))

