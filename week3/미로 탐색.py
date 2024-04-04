from collections import deque
N , M = map(int, input().split())
bfs_list = []
for _ in range(N) :
    bfs_list.append(list(map(int,input())))


def bfs(x,y) :
    bfs_list[x][y] = 0
    q = deque()
    cnt = 0
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    q.append([x,y])

    while q :
        x,y = q.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and bfs_list[nx][ny] == 1:
                q.append([nx, ny])
                bfs_list[nx][ny] = bfs_list[x][y] + 1



    return bfs_list[N-1][M-1]

print(bfs_list)


rst = 0
for i in range(N) :
    for j in range(M) :
        if bfs_list[i][j] == 1 :
            rst = max(rst, bfs(i,j))
print(bfs(0,0)+1)