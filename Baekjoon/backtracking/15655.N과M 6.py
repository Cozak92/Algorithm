n, m = list(map(int, list(input().split())))
candidate = list(map(int, list(input().split())))
arr = [0 for _ in range(m)]
isUsed = [False for __ in range(n)]

candidate.sort()

def fucn(k,index):

    if k == m:
        for i in range(m):
            print(arr[i], end=" ")
        print()
        return

    for i in range(index,n):
        if not isUsed[i]:
            arr[k] = candidate[i]
            isUsed[i] = True
            fucn(k+1,i+1)
            isUsed[i] = False

fucn(0,0)