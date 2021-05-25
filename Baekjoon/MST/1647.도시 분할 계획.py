import sys
from collections import defaultdict
sys.setrecursionlimit(10**6)
INF = sys.maxsize
input = sys.stdin.readline
def li(): return list(map(int,input().split()))

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


n,m = li()
union = [x for x in range(n+1)]
graph = sorted([li() for _ in range(m)], key= lambda x : x[2])

ans = 0
cnt = 0
for i in range(len(graph)):
    pos,dist = graph[i]
    x,y = pos
    if findRoot(x) != findRoot(y):
        cnt += 1
        ans += dist
        makeUnion(x,y)
    if cnt == n - 2:
        break

print(ans)