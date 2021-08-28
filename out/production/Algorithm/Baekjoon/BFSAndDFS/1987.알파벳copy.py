import sys
from collections import deque
INF = sys.maxsize
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
dir = [[0,1],[0,-1],[1,0],[-1,0]]

def li(): return list(map(int,input().split()))


r, c = li()
board = [[] for _ in range(r)]
for i in range(r):
    temp = input()
    for t in temp:
        board[i].append(t)
ans = -1
cache = 1 << ord(board[0][0]) - ord("A")

def dfs(x,y,cnt,cache):
    global ans
    ans = max(cnt,ans)
    
    for dx,dy in dir:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < r and 0 <= ny < c:
            if not cache & 1 << ord(board[nx][ny]) - ord("A"):
                nextCache = 1 << (ord(board[nx][ny]) - ord("A"))
                dfs(nx,ny,cnt+1,nextCache | cache)


dfs(0,0,1,cache)
print(ans)

