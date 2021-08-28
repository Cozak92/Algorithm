from collections import defaultdict
import sys
sys.setrecursionlimit(10**9)

input = sys.stdin.readline

def dfs(current):
    isVisited[current] = True
    dp[current][0] = 0
    dp[current][1] = weight[current-1]

    for adjNode in tree[current]:
        if not isVisited[adjNode]:
            dfs(adjNode)
            dp[current][0] += max(dp[adjNode][1],dp[adjNode][0])
            dp[current][1] += dp[adjNode][0]



n = int(input())

weight = list(map(int, list(input().split())))
dp = [[0,0] for _ in range(n+1)]
isVisited = [False] * (n+1)
tree = defaultdict(list)

for _ in range(n-1):
    a, b = map(int, list(input().split()))
    tree[a].append(b)
    tree[b].append(a)

dfs(1)
#print(dp)


print(max(dp[1][0],dp[1][1]))


