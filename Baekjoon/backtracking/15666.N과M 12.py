n, m = list(map(int, list(input().split())))
candidate = list(map(int, list(input().split())))
arr = [0 for _ in range(m)]
isUsed = [False for __ in range(n)]
candidate.sort()

def fucn(k,last):
    global isUsed

    if k == m:
        for i in range(m):
            print(arr[i], end=" ")
        print()
        return

    prev = -1

    for i in range(n):
        if not isUsed[i] and candidate[i] != prev and last <= i:
            arr[k] = candidate[i]
            prev = candidate[i]
            fucn(k+1,i)

    
fucn(0,0)