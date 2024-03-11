from collections import deque

lis = []
node, line , start = map(int,input().split())
visited = [0] * (node+1)
visited2 = [0] * (node+1)
q = deque()
def dfs(v) :
    visited[v] = 1 #방문처리
    print(v, end = " ")

    for i in graph[v] :
        if not visited[i] :
            dfs(i)
def bfs(v) :

    q.append(v)
    visited2[v] = 1
    while q :
        v = q.popleft()
        print(v, end = " ")
        for i in graph2[v] :
            if not visited2[i] :
                q.append(i)
                visited2[i] = 1


graph = [[] for i in range(node+1)]

for _ in range(line) :
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph :
    i.sort()

graph2 = graph.copy()
dfs(start)
print()
bfs(start)
