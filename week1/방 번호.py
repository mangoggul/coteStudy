
N = input()
nArr = [0]*10
for i in N :
    nArr[int(i)] += 1
for i in range(10) :
    if i == 6 or i == 9:
        if nArr[i] % 2 == 0 :
            nArr[i] = nArr[i] // 2
        else :
            nArr[i] = nArr[i] // 2 + 1
        if nArr[i] == 1:
            nArr[i] = 2

print(max(nArr))
#실패