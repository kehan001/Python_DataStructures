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

def find(distance, visit):
    min = float('inf')
    vertexIndex = None
    for i in range(n):
        if(visit[i] == 0 and distance[i] < min):
            min = distance[i]
            vertexIndex = i
    return vertexIndex

def Dijkstra(G, begin):
    visit = [0] * n #顶点是否被走过
    path = [-1] * n #路径
    distance = [0] * n #begin到达每一个顶点最短的距离

    for i in range(n): #将V0离所有顶点的距离赋值给distance
        distance[i] = G[begin][i]
    visit[begin] = 1
    distance[begin] = 0
    for i in range(n):
        if i != begin and distance[i] < float('inf'):
            path[i] = begin

    for i in range(n-1):
        next = find(distance, visit) #找当前权值最小路径中未被访问过的顶点
        visit[next] = 1 #更新访问
        for j in range(n): #目前来看Vj到V0的最小路径中Vj的上一个顶点是谁
            if(visit[j] == 0 and distance[next] + G[next][j] < distance[j]):
                distance[j] = distance[next] + G[next][j]
                path[j] = next
    return distance, path

#遍历路径
def showPath(distance, path, end):
    next = end
    trail = [end]
    while path[next] != -1:
        trail.append(path[next])
        next = path[next]
    trail.reverse()
    line = ""
    for i in range(len(trail)):
        if i != len(trail) - 1:
            line += (vertex[trail[i]] + " -> ")
        else:
            line += vertex[trail[i]]
    print(line)
    print(f"Total distance = {distance[end]}")

begin = 0
end = 8
sp = Dijkstra(graph, begin)
showPath(sp[0], sp[1], end)


