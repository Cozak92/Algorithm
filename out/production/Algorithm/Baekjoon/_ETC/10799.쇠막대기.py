import sys

input = sys.stdin.readline

factory = input().rstrip()
stack = []
answer = 0
prev = ""

for x in factory:
    #print(x)
    if x == "(":

        stack.append(x)
    else:
        top = stack.pop()
        if prev == "(":
            #print(len(stack))
            answer += len(stack)
        else:
            answer += 1
            
    prev = x

print(answer)
