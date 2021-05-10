from collections import deque
import sys
dx = [0,0,1,-1]
dy = [1,-1,0,0]
n, m = list(map(int, list(input().split())))
board = [[] for _ in range(n)]

for i in range(n):
    temp = list(map(int,list(input())))
    for t in temp:
        board[i].append(t)

q = deque()
q.append((0,0,0,1))
visited = [[[False for ___ in range(2)] for _ in range(m)] for __ in range(n)]
visited[0][0][0] = True

ans = sys.maxsize
while q:
    print(q)
    x,y,wall,dist = q.popleft()
    visited[x][y][wall] = True
    if x == n -1 and y == m - 1:
        ans = min(ans,dist)
        continue


    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny][wall]:
            if board[nx][ny] and not wall:
                visited[nx][ny][wall] = True
                q.append((nx,ny,wall+1,dist+1))
            elif not board[nx][ny]:
                visited[nx][ny][wall] = True
                q.append((nx,ny,wall,dist+1))
print((ans if ans != sys.maxsize else -1))