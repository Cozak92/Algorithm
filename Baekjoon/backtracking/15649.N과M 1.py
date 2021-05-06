n, m = list(map(int,list(input().split())))
isUsed = [False for _ in range(n+1)]
arr = [0 for _ in range(m)]
def func(k):

    if k == m:
        for j in range(m):
            print(arr[j], end=" ")
        print()
        return
    
    for i in range(1,n+1):
        if not isUsed[i]:
            arr[k] = i
            isUsed[i] = True
            func(k+1)
            isUsed[i] = False
func(0)
