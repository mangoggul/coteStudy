N = int(input())

Narr = list(map(int,input().split()))
want = int(input())
Narr.sort()

start = 0
last = N - 1
cnt = 0
while True :

    if last <= start :
        break
    sum = Narr[start] + Narr[last]
    if sum == want :
        last -= 1
        cnt += 1
    elif sum < want :
        start += 1
    elif sum > want :
        last -= 1

print(cnt)
