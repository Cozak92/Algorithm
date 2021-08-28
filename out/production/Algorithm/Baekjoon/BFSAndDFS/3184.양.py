import sys
from collections import deque
INF = sys.maxsize
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
MOD = 1000000007
dy = [1, 0, -1, 0]
dx = [0, -1, 0, 1]
dy8 = [1, 1, 0, -1, -1, -1, 0, 1]
dx8 = [0, -1, -1, -1, 0, 1, 1, 1]

def li(): return list(map(int,input().split()))


field = []


def bfs(r,c):
    global wolves,sheeps
    isVisited = [[False for _ in range(c)] for __ in range(r)]
    q = deque()
    
    for i in range(r):
        for j in range(c):
            if not isVisited[i][j] and field[i][j] != '#':
                q.append((i,j))
                isVisited[i][j] = True
                curSheeps,curWolves = 0,0
                if(field[i][j] == 'o'): curSheeps += 1
                if(field[i][j] == 'v'): curWolves += 1

                while q:

                    x, y = q.popleft()

                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]

                        if 0 <= nx < r and 0 <= ny < c and field[nx][ny] != '#':
                            if not isVisited[nx][ny]:
                                if(field[nx][ny] == 'o'): curSheeps+=1
                                if(field[nx][ny] == 'v'): curWolves += 1
                                q.append((nx,ny))
                                isVisited[nx][ny] = True
                if(curSheeps > curWolves): wolves -= curWolves
                else: sheeps -= curSheeps



r, c = li()
field = [input() for _ in range(r)]
sheeps,wolves = 0,0
for i in range(r):
    for j in range(c):
        if(field[i][j] == 'o'): sheeps+=1
        if(field[i][j] == 'v'): wolves+=1
bfs(r,c)
print(sheeps,wolves)




