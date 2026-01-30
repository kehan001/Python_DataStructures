vertex = ["V0", "V1", "v2", "V3", "V4", "V5", "V6", "V7", "V8"]
n = 9

graph = []
for i in range(n):
    graph.append([])
    for j in range(n):
        if i == j:
            graph[i].append(0)
        else:
            graph[i].append(float('inf'))

#赋值
graph[0][1] = 1
graph[0][2] = 5

graph[1][2] = 3
graph[1][3] = 7
graph[1][4] = 5

graph[2][4] = 1
graph[2][5] = 7

graph[3][4] = 2
graph[3][6] = 3

graph[4][5] = 3
graph[4][6] = 6
graph[4][7] = 9

graph[5][7] = 5

graph[6][7] = 2
graph[6][8] = 7

graph[7][8] = 4

#对称
for i in range(n):
    for j in range(i+1, n):
        graph[j][i] = graph[i][j]

def Floyd(G):
    distance = [[0] * n for _ in range(n)]
    path = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            distance[i][j] = G[i][j]
            path[i][j] = j
    for k in range(n): #中间点
        for i in range(n): #起点
            for j in range(n): #终点
                if distance[i][j] > distance[i][k] + distance[k][j]:
                    distance[i][j] = distance[i][k] + distance[k][j]
                    path[i][j] = path[i][k]
    return path


def getPath(start, end):
    path = Floyd(graph)
    shortestPath = [vertex[start]]
    while start != end:
        start = path[start][end]
        shortestPath.append(vertex[start])
    return " -> ".join(shortestPath)

print(getPath(0, 8))
