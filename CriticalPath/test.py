from CriticalPath.node import node
from CriticalPath.vertexNode import vertexNode
from Stack_UseArr.StackClass import Stack

vertex = []
n = 10
for i in range(n):
    vertex.append(f"V{i}")

adj_graph = []
for i in range(n):
    adj_graph.append([])
    for j in range(n):
        if i == j:
            adj_graph[i].append(0)
        else:
            adj_graph[i].append(float('inf'))

adj_graph[0][1] = 3
adj_graph[0][2] = 4
adj_graph[1][3] = 5
adj_graph[1][4] = 6
adj_graph[2][3] = 8
adj_graph[2][5] = 7
adj_graph[3][4] = 3
adj_graph[4][6] = 9
adj_graph[4][7] = 4
adj_graph[5][7] = 6
adj_graph[6][9] = 2
adj_graph[7][8] = 5
adj_graph[8][9] = 3

#邻接矩阵转邻接表
vnode = []
for i in range(n):
    vnode.append(vertexNode(i))
def to_adj_list(G):
    global vnode
    for i in range(n):
        for j in range(n):
            if G[i][j] != 0 and G[i][j] < float('inf'):
                newNode = node(j, G[i][j])
                newNode.next = vnode[i].next
                vnode[i].next = newNode
                vnode[j].entry += 1
to_adj_list(adj_graph)

def criticalPath(vnode):
    stack1 = Stack()
    stack2 = Stack()
    etv = [0] * n
    ltv = [0] * n
    for i in range(n):
        if vnode[i].entry == 0:
            stack1.push(vnode[i])

    while not stack1.isEmpty():
        curr = stack1.pop()
        stack2.push(curr)
        e = curr.next
        while e:
            k = e.data
            vnode[k].entry -= 1
            if vnode[k].entry == 0:
                stack1.push(vnode[k])
            if etv[k] < e.weight + etv[curr.data]: #经过curr，e到起点的路径是否变得更大了
                etv[k] = e.weight + etv[curr.data]
            e = e.next
    #ltv初始化，存最后一个顶点etv的值
    for i in range(n):
        ltv[i] = max(etv)
    while not stack2.isEmpty():
        curr = stack2.pop()
        e = curr.next
        while e:
            k = e.data
            if ltv[curr.data] > ltv[k] - e.weight:
                ltv[curr.data] = ltv[k] - e.weight
            e = e.next

    return etv, ltv

#创建关键子图
def build_critical_subgraph(vnode):
    etv, ltv = criticalPath(vnode)
    criticalGraph = [[] for _ in range(n)]
    for i in range(n):
        e = vnode[i].next
        while e:
            k = e.data
            if etv[i] == ltv[k] - e.weight:
                criticalGraph[i].append(k)
            e = e.next
    return criticalGraph

#DFS遍历
def showPath(vnode, start, end):
    criticalGraph = build_critical_subgraph(vnode)
    paths = []
    path = [start]
    def DFS(u):
        if u == end:
            paths.append(path.copy())
            return
        for i in criticalGraph[u]:
            path.append(i)
            DFS(i)
            path.pop()
    DFS(start)
    return paths

paths = showPath(vnode, 0, 9)
for path in paths:
    print(" -> ".join(vertex[j] for j in path))




