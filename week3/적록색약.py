from collections import deque
N = int(input())

graph = []
visited = [[False]*N for i in range(N)]
def bfs(x,y) :
    cnt = 0
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    q = deque()
    q.append([x,y])
    while q :
        X, Y = q.popleft()
        for i in range(4) :
            nx = X + dx[i]
            ny = Y + dy[i]
            if 0 <= nx < N and 0 <= ny < N :
                if graph[nx][ny] == 'R' :
                    q.append([nx,ny])
                    cnt += 1
    return cnt
rst = 0
for i in range(N) :
    graph.append(list(input()))
print(graph)
for i in range(N) :
    for j in range(N) :
        rst = bfs(i,j)

print(rst)