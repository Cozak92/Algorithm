#백준 2193

# N=1 : 1 (1가지)

# N=2 : 10 (1가지)

# N=3 : 101, 100 (2가지)

# N=4 : 1010, 1000, 1001, (3가지)

# N=5 : 10100, 10000, 10010, 10101, 10001 (5가지)

# N=6 : 101000, 100000, 100100, 101010, 100010, 101001, 100001, 100101 (8가지)

# N자리 이친수의 종류는 N-1자리 이친수 종류와 N-2자리 이친수 종류의 합으로 표현이 되고있습니다


# N자리 이친수는 두가지
# 1. N-1자리 이친수에 0을 추가한 경우
# 2. N-2자리 이친수에 01을 추가한 경우

def solution(N):

   
    dp = [0, 1, 1]
    for n in range(3,N+1):
        dp.append(dp[n-1] + dp[n-2])
         
    return dp[N]

print(solution(int(input())))