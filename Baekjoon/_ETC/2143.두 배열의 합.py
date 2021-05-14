# import sys
# import copy
# from collections import defaultdict
# INF = sys.maxsize
# input = sys.stdin.readline
# sys.setrecursionlimit(10**6)

# t = int(input())
# n = int(input())
# arr1 = list(map(int,input().split()))
# m = int(input())
# arr2 = list(map(int,input().split()))

# ans = 0
# SUM1 = copy.deepcopy(arr1)
# SUM2 = copy.deepcopy(arr2)
# for i in range(n-1):
#     SUM1[i+1] += SUM1[i]
# for j in range(m-1):
#     SUM2[j+1] += SUM2[j]
# SUM1 = [0] + SUM1
# SUM2 = [0] + SUM2
# left1 = 0
# left2 = 0
# right1 = 1
# right2 = 1
# while left1 <= n:
#     temp = SUM1[right1] - SUM1[left1]
#     print("-----1-----")
#     print(left1,right1)
#     if temp > t:
#         left1 += 1
#         continue
#     else:
#         if right1 == n -1:
#             left1 += 1
#         else: right1 += 1
#     while left2 <= m:
#         print("-----2-----")
#         print(left2,right2)
#         temp += SUM2[right2] - SUM2[left2]
#         print("TEMP",temp)
#         if temp == t:
            
#             ans += 1
#         elif temp > t:
#             left2 += 1
#         else:
#             if right2 == m -1:
#                 left2 += 1
#             else: right2 += 1


# print(ans)

import sys
import copy
from collections import defaultdict
INF = sys.maxsize
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


t = int(sys.stdin.readline())

n = int(sys.stdin.readline())
listA = list(map(int, input().split()))
m = int(sys.stdin.readline())
listB = list(map(int, input().split()))
table = defaultdict(int)


ans = 0

for i in range(n):
    for j in range(i, n):
        table[sum(listA[i:j+1])] += 1

for i in range(m):
    for j in range(i, m):
        ans += table[t - sum(listB[i:j+1])]

print(ans)