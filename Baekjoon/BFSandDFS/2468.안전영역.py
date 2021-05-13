from collections import deque

n = int(input())
board = [list(map(int,list(input().split()))) for _ in range(n)]
visited = [[False for _ in range(n)] for __ in range(n)]
dx = [0,0,1,-1]
dy = [1,-1,0,0]
safetyZone = - 1
for rain in range(1,101):
    temp = 0
    visited = [[False for _ in range(n)] for __ in range(n)]
    q = deque()
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and board[i][j] >= rain:
                q.append((i,j))
                visited[i][j] = True
   
                while q:
                    x,y = q.popleft()
                    visited[x][y] = True

                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]

                        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                            if board[nx][ny] >= rain:
                                q.append((nx,ny))
                                visited[nx][ny] = True
                temp += 1
    safetyZone = max(temp, safetyZone)

print(safetyZone)
    
