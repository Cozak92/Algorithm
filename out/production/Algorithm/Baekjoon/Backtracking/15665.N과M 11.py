n, m = list(map(int, list(input().split())))
candidate = list(map(int, list(input().split())))
arr = [0 for _ in range(m)]
isUsed = [False for __ in range(n)]
candidate.sort()

def fucn(k):
    global isUsed

    if k == m:
        for i in range(m):
            print(arr[i], end=" ")
        print()
        return

    prev = -1

    for i in range(n):
        if not isUsed[i] and candidate[i] != prev:
            arr[k] = candidate[i]
            prev = candidate[i]
            isUsed[i] = True
            fucn(k+1)
            isUsed[i] = False
    
fucn(0)