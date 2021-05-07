import sys
import collections

input = sys.stdin.readline
line = collections.deque()

def dfs(start):

    checked[start] = True

    #print("start = ", start)

    for e in node[start]:
        if not checked[e]:
            #print("I =" , i)
            checked[i] = True
            line.appendleft(dfs(e))

    return start

N, M = map(int,list(input().split()))
checked = [False] * (N+1)

node = [ [] for __ in range(N+1)]

for i in range(M):
    x, y = map(int,list(input().split()))

    node[x].append(y)

#print(node)

for i in range(1,N+1):
    if not checked[i]:
        line.appendleft(dfs(i))


for x in line:
    print(x, end=' ')