import sys
input = sys.stdin.readline

n = int(input())

# dp[i][j] = i부터 j까지 회문이 가능한지
# 양쪽 끝을 확인하고 사이에 있는값이 회문이 가능하다면 1

arr = list(map(int, list(input().split())))

dp = [[0 for _ in range(n)] for __ in range(n)]

for i in range(n):
    dp[i][i] = 1
for i in range(n-1):
    if arr[i] == arr[i+1]:
        dp[i][i+1] = 1
        

for i in range(2,n):

    for j in range((n-i)):

        if arr[j] == arr[j+i] and dp[j+1][j+i-1]:
            dp[j][j+i] = 1

#print(dp)

m = int(input())

for i in range(m):
    start, end = list(map(int, list(input().split())))

    print(dp[start-1][end-1])


# 5
# 1 4 1 2 1
# 4
# 1 3
# 3 5
# 1 5
# 2 4
        

