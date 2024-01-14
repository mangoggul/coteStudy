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

#two pointer 알고리즘
#첫번째를 start 마지막을 last
#sum 과 찾는 것이 같다면 last -= 1 cnt += 1
#sum 이 찾는 것보다 작다면 start += 1
#sum 이 찾는 것보다 크다면 last -= 1

