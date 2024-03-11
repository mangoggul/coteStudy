from collections import deque
size = int(input())
vertex = int(input())
bfs_list = [[]*(size+1) for _ in range(size + 1)]
visited = [0]*(size+1)
for _ in range(vertex) :
    n, m = map(int,input().split())
    bfs_list[n].append(m)
    bfs_list[m].append(n)
def bfs(v) :
    cnt = 0
    q = deque()
    q.append(v)
    visited[v] = 1
    while q :
        que = q.popleft()
        #print(que, end = " ")
        for i in bfs_list[que]:
            if not visited[i]:
                q.append(i)
                visited[i] = 1
                cnt += 1
    return cnt

print(bfs(1))