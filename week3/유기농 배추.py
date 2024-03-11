from collections import deque
cnt = 0
trial = int(input())
def bfs(x, y) :
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
            if 0 <= nx < sero and 0 <= ny < garo and bfs_list[nx][ny] == 1 :
                q.append([nx,ny])
                bfs_list[nx][ny] = 0


for _ in range(trial) :
    sero, garo, N = map(int,input().split())
    bfs_list = [[0] * garo for _ in range(sero)]
    for i in range(N) :
        x, y = map(int,input().split())
        bfs_list[x][y] = 1
    for i in range(sero):
        for j in range(garo):
            if bfs_list[i][j] == 1 :
                bfs(i,j)
                cnt+= 1
    print(cnt)
    cnt = 0

