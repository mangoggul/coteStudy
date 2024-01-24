from collections import deque
import sys
input = sys.stdin.readline


flag = 0
rev_cnt = 0
del_cnt = 0
N = int(input())
for i in range(N) :
    AC = input()
    size = int(input())
    arr = deque(input().rstrip()[1:-1].split(","))

    for ins in AC :
        if ins == 'R' :
            rev_cnt += 1
        elif ins == 'D' :
            if len(arr) == 0 or size == 0:
                print("error")
                rev_cnt = 0
                break
            else :
                if rev_cnt % 2 == 0 :
                    arr.popleft()
                else :
                    arr.pop()


        else :
            if rev_cnt % 2 == 0:
                print("[" + ",".join(arr) + "]")
                rev_cnt = 0
            else :
                arr.reverse()
                print("[" + ",".join(arr) + "]")
                rev_cnt = 0


