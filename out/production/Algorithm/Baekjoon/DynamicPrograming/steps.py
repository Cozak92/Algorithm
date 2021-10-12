#백준 2579번


# DP[N] = MAX( STEP[N-1] + STEP[N] + DP[N-3] , DP[N-2] + STEP[N])


def cal():

    for n in range(3,len(steps)):
        dp[n] = max( steps[n-1] + steps[n] + dp[n-3] , dp[n-2] + steps[n])

    return dp[-1]



N = int(input())
steps = []
for i in range(N):
    steps.append(int(input()))

dp = [0] * N

dp[0] = steps[0]

dp[1] = steps[0] + steps[1]

dp[2] = max(steps[1] + steps[2], steps[0] + steps[2])

print(cal())



