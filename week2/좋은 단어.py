

size = int(input())
stack = []
cnt = 0
for _ in range(size) :
    sample = input()
    for i in range(len(sample)) :
        tmp = sample[i]

        if not stack :
            stack.append(sample[i])
        else :
            if tmp == stack[-1] :
                stack.pop()

            else :
                stack.append(sample[i])


    if not stack :
        cnt += 1
    stack = []

print(cnt)

