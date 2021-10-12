import bisect
from collections import deque
import sys

input = sys.stdin.readline

n = int(input())

arr = list(map(int,input().split()))

stack = []
tracking = []
stack.append(arr[0])
tracking.append((0,arr[0]))

for i in range(1,n):

    if stack[-1] < arr[i]:
        stack.append(arr[i])
        tracking.append((len(stack)-1, arr[i]))
    else:
        index = bisect.bisect_left(stack,arr[i])
        stack[index] = arr[i]
        tracking.append((index,arr[i]))


answer = deque()
index = len(stack) -1

for k in range(len(tracking)-1,-1,-1):
    i,v = tracking[k]
    if index == i:
        answer.appendleft(v)
        index -= 1

print(len(answer))
# print(answer)
print(*answer)
