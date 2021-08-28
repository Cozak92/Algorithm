
n , m = list(map(int,input().split()))
arr = [0 for _ in range(m)]
isUsed = [False for _ in range(n+1)]

def func(k,last):

    if k == m:
        for j in range(m):
            print(arr[j], end= " ")
        print()
        return
    
    for i in range(1,n+1):
        if not isUsed[i] and last <= i:
            arr[k] = i
            func(k+1,i)
    

func(0,0)