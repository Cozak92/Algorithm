import sys
from collections import defaultdict
INF = sys.maxsize
sys.setrecursionlimit(10**9)

def findRoot(x):

    if union[x] == x:
        return x

    union[x] = findRoot(union[x])
    return findRoot(union[x])

def uniona(a, b):
    a = findRoot(a)
    b = findRoot(b)
    
    if b < a:
        union[a] = b
    else:
        union[b] = a



v, e = list(map(int, list(input().split())))

graph = defaultdict(int)
union =[0] + [i for i in range(1,v+1)]



for i in range(e):
    a, b, c = list(map(int, list(input().split())))

    graph[(a,b)] = c

graph = dict(sorted(graph.items(), key= lambda x: x[1]))

#print(graph)
#print(union)
SUM = 0

for x,y in graph:
    #print(x,y)
    #print(union[x],union[y])
    
    if findRoot(x) != findRoot(y):
        #print(x,y)
        uniona(x, y)
        SUM += graph[(x,y)]

print(SUM)