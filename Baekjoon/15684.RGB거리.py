# 문제좀 제대로 읽읍시다

def dfs(index,color):
    if index > n:
        return 0

    if dp[index][color] != INF:
        return dp[index][color]

        
    for c in colorSet:
        if c != color:
            dp[index][color] = min(dp[index][color],dfs(index + 1,c) + houses[index][color])
    

    return dp[index][color]


import sys
sys.setrecursionlimit(10**9)

INF = sys.maxsize

input = sys.stdin.readline

n = int(input())

houses = [[0]]

colorSet = [0,1,2]

dp = [[INF for _ in range(3)] for __ in range(n + 1)]

for i in range(n):
    houses.append( list(map(int, list(input().split()))))


print(min(dfs(1,0),dfs(1,1),dfs(1,2)))

#print(dp)
