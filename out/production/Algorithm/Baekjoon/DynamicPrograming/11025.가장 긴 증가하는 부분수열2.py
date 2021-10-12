import sys
import bisect
input = sys.stdin.readline
n = int(input())
arr = list(map(int,input().split()))
stack = []
stack.append(arr[0])
for num in arr :
    if num > stack[-1]:stack.append(num)
    else:bisect.insort_left(arr,num)
print(len(stack))

# answer = deque()
# index = len(stack) - 1
# for i in range(len(track)-1,-1,-1):
#     i, v= track[i]
#     if i == index:
#         answer.appendleft(v)
#         index -= 1

# print(*answer)