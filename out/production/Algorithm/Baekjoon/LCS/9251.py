import sys

input = sys.stdin.readline


N = input()
A = input().split()
B = input().split()

dp = [[ 0 for _ in range(len(B)+1)] for __ in range(len(A)+1)]
#print(dp)


for i in range(len(A)):
    for j in range(len(B)):
        if A[i] == B[j]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j],dp[i][j-1])

#print(dp)

print(dp[len(A)-1][len(B)-1])
