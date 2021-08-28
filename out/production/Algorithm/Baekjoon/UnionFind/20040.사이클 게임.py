import sys
input = sys.stdin.readline

def findRoot(x):
    if union[x] == x:
        return x
    union[x] = findRoot(union[x])

    return findRoot(union[x])

def makeUnion(a,b):

    rootA = findRoot(a)
    rootB = findRoot(b)

    if rootA < rootB:
        union[rootB] = rootA
    else:
        union[rootA] = rootB

n, m = list(map(int,input().split()))
union = [x for x in range(n)]
order = [list(map(int,input().split())) for _ in range(m)]
for i in range(1,m+1):
    a,b = order[i-1]

    if findRoot(a) == findRoot(b):
        print(i)
        exit()
    
    else:
        makeUnion(a,b)

print(0)


    