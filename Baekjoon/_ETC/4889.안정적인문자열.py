
index = 0
while True: 
    index += 1
    s = input()

    if s.startswith("-"):
        break
    cnt = 0
    stack = []
    for b in s:
        if b == "{":
            stack.append(b)
        else:
            if(stack):
                stack.pop()
            else:
                stack.append("{")
                cnt += 1
            
    if stack:
        cnt += len(stack) // 2
    
    print(str(index)+".",cnt)

