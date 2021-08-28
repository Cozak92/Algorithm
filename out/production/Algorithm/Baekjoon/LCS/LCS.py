

# for i in range(len(A)):
#     for j in range(len(B)):
#         if A[i] == B[i]:
#             dp[i][j] == dp[i-1][i-j] + 1
#             result = max(dp[i][j],result)




# for i in range(len(A)):
#     for j in range(len(B)):
#         if A[i] == B[i]:
#             dp[i][j] == dp[i-1][i-j] + 1
#             result = max(dp[i][j],result)

#         else:
#             dp[i][j] = max(dp[i-1][j],dp[i][j-1])

# print(dp[N][M])

i, j = n, m
result = ""
while i == 0 or j == 0:

    if dp[i][j] == dp[i-1][j]:
        i -= 1
    elif dp[i][j] == dp[i][j-1]:
        j -= 1
    else:
        result += A[i] #A문자열이나 B문자열 아무것이나 가져와서 넣으면 된다.
        i -= 1
        j -= 1

print(result[::-1])