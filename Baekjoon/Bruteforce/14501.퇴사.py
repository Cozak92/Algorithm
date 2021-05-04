n = int(input())
table = [[] for _ in range(n)]
dp = [-1 for _ in range(n)]

def dfs(day):
    if day >= n:
        return 0

    if dp[day] != -1:
        return dp[day]

    if day+1 > n or day+table[day][0] > n:
        return dfs(day+1)

    dp[day] = max(dfs(day+1), dfs(day+table[day][0])+table[day][1])

    return dp[day]

for i in range(n):

    table[i] = list(map(int,list(input().split())))

print(dfs(0))