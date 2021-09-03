n = int(input())
dp = [0] * (n+1)
track = [0] * (n+1)
track[1] = -1
dp[1] = 0
for i in range(2, n+1):
    dp[i] = dp[i-1] + 1
    track[i] = i - 1
    if i % 2 == 0 and dp[i//2] + 1 < dp[i]:
        dp[i] =  dp[i//2]+1
        track[i] = i//2
    if i % 3 == 0 and dp[i//3] + 1 < dp[i]:
        dp[i] = dp[i//3]+1
        track[i] = i//3
print(dp[n])

while n != -1:
    print(n, end= " ")
    n = track[n]