
from collections import deque
dfs_list = []


def bfs(x,y) :
    dfs_list[x][y] = 0
    dx = [1,-1,0,0] #우 좌 하 상
    dy = [0,0,1,-1]# 우 좌 하 상
    q = deque()
    cnt = 1
    q.append([x,y])

    while q:
        x,y = q.popleft()
        for i in range(4) :
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < N and 0 <= ny < M and dfs_list[nx][ny] == 1 :
                q.append([nx,ny])
                dfs_list[nx][ny] = 0
                cnt += 1
    return cnt

N , M = map(int,input().split())

for i in range(N) :
    dfs_list.append(list(map(int, input().split())))
size_cnt = 0
ans = 0
for i in range(N) :
    for j in range(M) :
        if dfs_list[i][j] == 1:
            size_cnt += 1
            ans = max(bfs(i,j),ans)
print(size_cnt)
print(ans)
