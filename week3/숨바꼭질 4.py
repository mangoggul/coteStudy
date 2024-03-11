from collections import deque

start, last = map(int,input().split())
# 5 17 start and last

def path(x) :
    arr = []
    temp = x #temp 는 지금 도착지점 == 17
    for _ in range(dist[x] + 1) : # depth + 1
        arr.append(temp) #17먼저 넣어
        temp = move[temp] #계속 왔다리갔다리~~
    print(' '.join(map(str, arr[::-1])))

def bfs() :
    q = deque() #make "q" deque
    q.append(start) #insert start in "Q"

    while q :
        v = q.popleft() #vertex를 뽑아서
        if v == last: #v 가 last까지 가면? -> dist[v]출력
            print(dist[v])
            path(v) #v == 마지막 도착 지점
            return v
        for i in (v*2, v+1, v-1) : #곱2 플1 마1

            if 0<=i<=100000 and dist[i] == 0 :#dist[i]를 방문하지 않앗다면
                q.append(i)
                dist[i] = dist[v] + 1
                move[i] = v



print(*move)
dist = [0]*100001
move = [0]*100001
bfs()
