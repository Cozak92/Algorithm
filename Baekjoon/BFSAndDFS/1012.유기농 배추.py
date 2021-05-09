import sys
from collections import deque
input = sys.stdin.readline
dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(cabbage):
    global field
    cnt = 0
    q = deque()
    isVisited = [[ 0 for _ in range(row+1)] for __ in range(column+1)]
    while cabbage:
        i,j = cabbage.pop()
        #print(i,j)
        if not isVisited[i][j]:
            q.append((i,j))
            isVisited[i][j] = True

            while q:

                x,y = q.popleft()
                isVisited[x][y] = True
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]

                    if 0 <= nx < column and 0 <= ny < row:
                        if field[nx][ny] == 1 and not isVisited[nx][ny]:
                            isVisited[nx][ny] = True
                            q.append((nx,ny))
            
            cnt += 1
    return cnt
    


t = int(input())

for i in range(t):

    row,column,k = list(map(int,input().split()))
    
    field = [[ 0 for _ in range(row+1)] for __ in range(column+1)]
    cabbage = []
    for i in range(k):
        y,x = list(map(int,input().split()))

        field[x][y] = 1
        cabbage.append((x,y))

    
    print(bfs(cabbage))