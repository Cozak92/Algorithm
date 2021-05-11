import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def findUnion(x):
    if arr[x] == x:
        return x
    
    arr[x] = findUnion(arr[x])

    return findUnion(arr[x])


def makeUnion(a, b):
    rootA,rootB = 0,0

    rootA = findUnion(a)
    rootB = findUnion(b)


    if rootA < rootB:
        arr[rootB] = rootA
    
    else:
        arr[rootA] = rootB

    

n, m = list(map(int,list(input().split())))
arr = [0] + [j for j in range(1,n+1)]

for i in range(m):
    order, a, b = list(map(int,list(input().split())))

    if order == 0:
        makeUnion(a,b)
    
    if order == 1:

        if findUnion(a) == findUnion(b):
            print("YES")
        else:
            print("NO")