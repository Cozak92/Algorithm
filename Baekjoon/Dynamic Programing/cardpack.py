#백준 11052번

# dp[1] == 1개를 사는데 최대값 buyCardpack[1] 

# dp[2] == 2개를 사는데 최대값 buyCardpack[2] or dp[1] + dp[1] 

# dp[3] == 3개를 사는데 최대값 buyCardpack[3] or dp[2] +dp[1]

# dp[4] == 4개를 사는데 최대값 buyCardpack[4] or dp[3] + dp[1] or dp[2]+ dp[2]

# dp[5] == 5개를 사는데 최대값 buyCardpack[5] or dp[4] +dp[1]...


# dp[n] = buyCardpack[n] or dp[n-i] +dp[i] .....



import math as m

def solution(N,buyCardpack,dp):

    for j in range(3,N+1):
        dp[j] = buyCardpack[j]
        for i in range(1 ,N//2 + 1):
            dp[j] = max(dp[j], dp[j-i]+dp[i])


    return print(dp[N])



N = int(input())
buyCardpack = [0]
buyCardpack += list(map(int, input().split()))
dp = [0] * (N+1)
dp[1] = buyCardpack[1]
dp[2] = max(buyCardpack[2], buyCardpack[1]*2)


solution(N,buyCardpack,dp)