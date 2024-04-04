import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline
N = int(input())
Narr = list(map(int, input().split()))
Narr.sort()# 이진 탐색을 위해 배열을 정렬합니다.

M = int(input())
Marr = list(map(int, input().split()))

for target in Marr :
    left , right = 0, N-1
    isExist = 0
    while left <= right :

        mid = (left + right) // 2
        if Narr[mid] == target :
            cnt = bisect_right(Narr, target) - bisect_left(Narr,target)
            isExist = 1
            print(cnt, end = " ")
            break
        elif Narr[mid] <= target :
            left = mid + 1
        else :
            right = mid -1
    if isExist == 0:
        print(0, end = " ")
