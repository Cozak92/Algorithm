import sys
import bisect

input = sys.stdin.readline
n = int(input())
arr = list(map(int,input().split()))

stack = [0] * n
stack[0] = arr[0]
for i in range(1,n):
    flag = True
    for j in range(i):
        if arr[j] < arr[i]:
            stack[i] = max(stack[i],arr[i] + stack[j])
        else:
            stack[i]=max(stack[i], arr[i])
print(max(stack))