X = input()
two, three = 1, 1
rst = 0
stack = []
for i in range(len(X)) :
    if X[i] == '(' :
        stack.append(X[i])
        if X[i-1] == ']' :
            rst += three
            print('쓰리 더해!!')
        elif X[i - 1] == ')':
            rst += two
            print('투우 더해!!')

    if X[i] == '[' :
        stack.append(X[i])
        if X[i-1] == ')' :
            rst += three
            print('쓰리 더해!!')
        elif X[i-1] == ']' :
            rst += three
            print('쓰리 더해!!')
    elif X[i] == ')' :
        if stack[-1] == '(' :
            stack.pop()
            two *= 2
            print('투우!')


    elif X[i] == ']':
        if stack[- 1] == '[':
            stack.pop()
            three *= 3
            print('쓰리!')

        el:
            rst += two
            print('투우 더해! ')

print(rst)

