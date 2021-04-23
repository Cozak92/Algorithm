from collections import deque
import sys
sys.setrecursionlimit(10**9)

def dist(a,b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])


def investigae(firstCop, secondCop):
    curCase = max(firstCop, secondCop) + 1
    if curCase == w+2: return 0

    if dp[firstCop][secondCop] != -1:
        return dp[firstCop][secondCop]

    X = investigae(curCase,secondCop) + dist(cases[firstCop],cases[curCase])
    Y = investigae(firstCop,curCase) + dist(cases[secondCop],cases[curCase])

    if X < Y :
        ans[firstCop][secondCop] = 1
    else:
        ans[firstCop][secondCop] = 2
    dp[firstCop][secondCop] = min(X,Y)
    
    return dp[firstCop][secondCop]




n = int(input())

w = int(input())
dp = [[-1 for _ in range(w+3)] for __ in range(w+3)]
ans = [[-1 for _ in range(n+1)] for __ in range(n+1)]
cases = []

cases.append([0,0])
cases.append([n,n])

for i in range(w):
    cases.append(list(map(int,list(input().split()))))

print(investigae(0,1))
print(cases)
print(dp)
print(ans)

x = 0
y = 1
while max(x, y) + 1 <= w+1:
    print(ans[x][y])
    if ans[x][y] == 1:
        x = max(x,y) + 1
    else:
        y = max(x,y) + 1