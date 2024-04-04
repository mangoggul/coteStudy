import sys

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

M = int(input())
Marr = list(map(int, input().split()))
A.sort()  # 이진 탐색을 위해 배열을 정렬합니다.

# def binary_search(arr, target):
#     start, end = 0, len(arr) - 1
#     while start <= end:
#         mid = (start + end) // 2
#         if arr[mid] == target:
#             return 1
#         elif arr[mid] < target:
#             start = mid + 1
#         else:
#             end = mid - 1
#     return 0

for target in Marr:
    left, right = 0, N-1
    isExist = 0
    while left <= right :
        mid = (left+right)//2
        if target == A[mid] :
            print(1)
            isExist = 1
            break
        elif target > A[mid] :
            left = mid + 1
        else :
            right = mid - 1
    if isExist == 0 :
        print(0)
