from collections import deque

a, b = map(int,input().split())
arr = deque(map(int,input().split()))
dq = deque(i+1 for i in range(a))
cnt = 0


for num in arr :
    while True:
        if dq[0] == num:
            dq.popleft()
            break
        else:
            if dq.index(num) <= len(dq)//2:
                dq.rotate(-1)
                cnt += 1
            else :
                dq.rotate(1)
                cnt += 1

print(cnt)