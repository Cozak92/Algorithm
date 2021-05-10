# dp[i][2] = max(dp[i-1][1]+step[i], dp[i-1][2])
# dp[i][1] = max(dp[i-1][0])
n = int(input())
step = [0] + [int(input()) for _ in range(n)]

if n == 1:
    print(step[1])
    exit()
# dp = [[0 for _ in range(5)] for __ in range(n+10)]
# dp[1][1] = step[1]
# dp[1][2] = 0
# dp[2][1] = step[2]
# dp[2][2] = step[2] + step[1]
# for i in range(3,n+1):
#     dp[i][1] = max(dp[i-2][1], dp[i-2][2])+ step[i]
#     dp[i][2] = dp[i-1][1] + step[i]
 
# print(max(dp[n][1],dp[n][2]))

dp = [0] + [0 for _ in range(n)]
dp[1] = step[1]
dp[2] = step[2]
dp[3] = step[3]

for i in range(4,n+1)