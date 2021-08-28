n, m = list(map(int, list(input().split())))
arr = list(map( int, list(input().split())))


ans = -1
# 완전탐색
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if arr[i] + arr[j] + arr[k] <= m:
                ans = max(ans,arr[i] + arr[j] + arr[k])

#dp

print(ans)