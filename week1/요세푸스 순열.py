from collections import deque
N , M = map(int,input().split())
dequeN = deque(i+1 for i in range(N))
rst = []
while dequeN :
    for _ in range(M -1) :
        dequeN.append(dequeN.popleft())
    rst.append(str(dequeN.popleft()))
print("<" + ", ".join(rst) + ">")

