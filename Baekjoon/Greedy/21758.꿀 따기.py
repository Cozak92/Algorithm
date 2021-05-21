import sys
import copy
INF = sys.maxsize
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
MOD = 1000000007
dy = [1, 0, -1, 0]
dx = [0, -1, 0, 1]
dy8 = [1, 1, 0, -1, -1, -1, 0, 1]
dx8 = [0, -1, -1, -1, 0, 1, 1, 1]

def li(): return list(map(int,input().split()))



n =int(input())
honey = li()

SUM = copy.deepcopy(honey)

for i in range(1,n):
    SUM[i] += SUM[i-1]

ans =-INF
for i in range(1,n-1):
     #벌통이 오른쪽에 있는 경우
    temp = SUM[n-1] + (SUM[n-1] - SUM[i])  - honey[0]  - honey[i]
    ans = max(ans,temp)
     #벌통이 가운데 있는 경우
    temp = SUM[n-1] - honey[0] - honey[n-1] + honey[i]
    ans = max(ans,temp)
    #벌통이 왼쪽에 있는 경우
    temp = SUM[n-1] + SUM[i] - honey[n-1] - (honey[i] *2)
    ans = max(ans,temp)

print(ans)

