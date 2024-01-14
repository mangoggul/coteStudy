from collections import deque

N = int(input())
myDeque = deque()
for _ in range(N) :
    n = int(input())
    if n == 0 :
        myDeque.pop()
    else :
        myDeque.append(n)
print(sum(myDeque))