import sys

input = sys.stdin.readline
#https://codeforces.com/contest/1516/problem/A

t = int(input())

for _ in range(t):

    arr = []

    n, k = map(int, list(input().split()))

    arr = list(map(int, list(input().split())))

    for i in range(n-1):

        if arr[i] < k:
            k -= arr[i]
            arr[n-1] += arr[i]
            arr[i] = 0
        else:
            arr[i] -= k
            arr[n-1] += k
            k = 0
    print(*arr)

    # for x in arr:     
    #     print(x, end = ' ')