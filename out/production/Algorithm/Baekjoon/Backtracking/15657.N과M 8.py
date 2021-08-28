n, m = list(map(int, list(input().split())))
candidate = list(map(int, list(input().split())))
arr = [0 for _ in range(m)]
isUsed = [False for __ in range(n)]

candidate.sort()

def fucn(k,last):

    if k == m:
        for i in range(m):
            print(arr[i], end=" ")
        print()
        return

    for i in range(n):
        if last <= i:

            arr[k] = candidate[i]
            fucn(k+1,i)
fucn(0,0)