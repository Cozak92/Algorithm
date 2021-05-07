t = int(input())



for _ in range(t):
    stack = []

    braket = input()
    flag = True
    for b in braket:

        if b == "(":
            stack.append(b)
        else:
            if not stack:
                print("NO")
                flag = False
                break
            else:
                stack.pop()
        #print(stack)
    if stack:
        print("NO")
        flag = False
    if flag : print("YES")