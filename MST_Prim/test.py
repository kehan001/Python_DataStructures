#顶点集
vertex = ["A", "B", "C", "D" ,"E" ,"F" ,"G", "H", "I"]
n = 9
# 初始化邻接矩阵（0 表示无边）
graph = []
for i in range(n):
    graph.append([])
    for j in range(n):
        if i == j:
            graph[i].append(0) #自环为0
        else:
            graph[i].append(float('inf')) #先赋值无穷大给无边的

# A-B  A-F
graph[0][1] = 10
graph[0][5] = 11
# B-C  B-G  B-I
graph[1][2] = 18
graph[1][6] = 16
graph[1][8] = 12
# C-D  C-I
graph[2][3] = 22
graph[2][8] = 8
# D-E  D-G  D-H  D-I
graph[3][4] = 20
graph[3][6] = 24
graph[3][7] = 16
graph[3][8] = 21
# E-F  E-H
graph[4][5] = 26
graph[4][7] = 7
# F-G
graph[5][6] = 17
# G-H
graph[6][7] = 19

#对称
for i in range(n):
    for j in range(i+1, n):
        graph[j][i] = graph[i][j]

def Prim(G):
    weight = [0]*n #记录备选路的权值
    vexIndex = [0]*n #表示值(出发点)与下标(到达点)之间有条路

    for i in range(n): #第一层A遍历
        weight[i] = graph[0][i]
        vexIndex[i] = 0
    u = 0  # 下一轮要遍历的顶点

    for j in range(1, n):
        #遍历weight选出目前最优路径
        min = float('inf')
        currIndex = 0
        for i in range(n):
            if(weight[i] != 0 and weight[i] < min):
                min = weight[i]
                currIndex = i
        u = currIndex
        weight[currIndex] = 0
        print(f"{vertex[vexIndex[currIndex]]}, {vertex[currIndex]}")

        #遍历当前行，替换weight和vexIndex
        for i in range(n):
            if(graph[u][i] != 0 and graph[u][i] < weight[i]):
                weight[i] = graph[u][i]
                vexIndex[i] = u

Prim(graph)

"""
for i in range(len(vertex)):
    for j in range(len(vertex)):
        print(graph[i][j], end=" ")
    print()
"""