from collections import deque
graph = []

N, M = map(int,input().split())
for _ in range(M) :
    graph.append(list(map(int, input().split())))
print(graph)
visited = [[0]*M for i in range(N)]
def bfs(x,y) :
    cnt = 0
    q = deque()
    nx = [1,-1,0,0]
    ny = [0,0,1,-1]
    q.append([x,y])
    for i in range(4) :
        dx = x + nx[i]
        dy = y + ny[i]
    while q :
        xPos, yPos = q.popleft()
        if graph[xPos][yPos] == 1 and nx <= M and ny <= N :

            q.append([xPos,yPos])
            cnt += 1
    return cnt
print(visited)

rst = 0
for i in range(N) :
    for j in range(M) :
        if graph[i][j] == 1 :
            rst = max(rst, bfs(i,j))
print(rst)

