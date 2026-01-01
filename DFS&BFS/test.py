#顶点集
vertex = ["A", "B", "C", "D" ,"E" ,"F" ,"G", "H", "I"]
n = 9
#初始化邻接矩阵
graph = []
for i in range(len(vertex)):
    graph.append([])
    for j in range(len(vertex)):
        graph[i].append(0)
# A-B  A-F
graph[0][1] = 1
graph[0][5] = 1
# B-C  B-G  B-I
graph[1][2] = 1
graph[1][6] = 1
graph[1][8] = 1
# C-D  C-I
graph[2][3] = 1
graph[2][8] = 1
# D-E  D-G  D-H  D-I
graph[3][4] = 1
graph[3][6] = 1
graph[3][7] = 1
graph[3][8] = 1
# E-F  E-H
graph[4][5] = 1
graph[4][7] = 1
# F-G
graph[5][6] = 1
# G-H
graph[6][7] = 1

#对称
for i in range(len(graph)):
    for j in range(len(graph)):
        graph[j][i] = graph[i][j]

#深度优先
visit = [0 for i in range(len(vertex))] #访问数组
def DFS(G, index):
    visit[index] = 1
    print(vertex[index], end=" ")  # 输出节点
    for i in range(n): #遍历当前行
        if(visit[i] == 0 and G[index][i] == 1): #如果没有被访问并且与当前节点有链接则递归
            DFS(G, i)

#广度优先
def BFS(G):
    visit = [0]*n
    queue = [0] #创建队列
    visit[0] = 1 #更新访问状态
    while queue: #当队列不为空时
        curr = queue.pop(0)
        print(vertex[curr], end=" ")
        for i in range(n): #遍历矩阵当curr行的所有值
            if G[curr][i] == 1 and visit[i] == 0:
                visit[i] = 1
                queue.append(i)


print("DFS: ", end="")
DFS(graph, 0)
print("\nBFS: ", end="")
BFS(graph)

"""
for i in range(len(vertex)):
    for j in range(len(vertex)):
        print(graph[i][j], end="")
    print()
"""
