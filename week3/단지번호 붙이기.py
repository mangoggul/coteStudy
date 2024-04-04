from collections import deque

row = int(input())
graph = []
for _ in range(row) :
    graph.append(list(map(int,input())))
print(graph[0][0])

def bfs(x,y) :
    q = deque()
    cnt = 0
    q.append(graph[x,y])
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    x,y = q.popleft()
    for i in range(4) :
        nx = dx[i] + x
        ny = dy[i] + y
        if 0 <= nx <= row and 0 <= ny <= row and graph[nx][ny] == 1 :
            q.append([nx,ny])
            graph[nx][ny] = 0
            cnt += 1