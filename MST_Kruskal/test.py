#顶点集
from MST_Kruskal.edge import edge

vertex = ["A", "B", "C", "D" ,"E" ,"F" ,"G", "H", "I"]
n = 9
# 初始化邻接矩阵（0 表示无边）
graph = []
for i in range(n):
    graph.append([])
    for j in range(n):
        if(i == j):
            graph[i].append(0)
        else:
            graph[i].append(float('inf'))
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

#存放当前顶点的上级
parent = [0] * n

#寻找当前顶点所在的树中的根，每一次都是找上级
def find(parent, index):
    while(parent[index] > 0):
        index = parent[index]
    return index

def kruskal(G):
    #创建edge集合
    edges = []
    for i in range(n):
        for j in range(i+1, n):
            if(G[i][j] < float('inf')):
                edges.append(edge(i, j, G[i][j]))
    edges.sort(key=lambda e: e.weight) #小-大

    for i in range(len(edges)):
        x = find(parent, edges[i].begin)
        y = find(parent, edges[i].end)
        if(x != y):
            parent[x] = y
            print(f"{vertex[edges[i].begin]} - {vertex[edges[i].end]} - weight - {edges[i].weight}")

kruskal(graph)