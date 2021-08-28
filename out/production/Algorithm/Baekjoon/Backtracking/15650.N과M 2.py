n , m = list(map(int,input().split()))
arr = [0 for _ in range(m)]
isUsed = [False for _ in range(n+1)]

def func(index,k):

    if k == m:
        for j in range(m):
            print(arr[j], end= " ")
        print()
        return
    
    for i in range(index,n+1):
        if not isUsed[i]:

            arr[k] = i
            isUsed[i] = True
            func(i+1,k+1)
            isUsed[i] = False
    

func(1,0)