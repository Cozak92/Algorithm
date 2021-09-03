import sys
input = sys.stdin.readline
n, m = list(map(int, input().split()))
arr = list(map(int,input().split()))

for i in range(1,n):
    arr[i] += arr[i-1]
print(arr)
for k in range(m):
    i,j = list(map(int, input().split()))
    if i == 1:
        print(arr[j-1])
    else:
        print(arr[j - 1] - arr[i - 2])