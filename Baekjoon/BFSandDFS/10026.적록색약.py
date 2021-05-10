from collections import deque
import copy
dx = [0,0,1,-1]
dy = [1,-1,0,0]

def normalBFS():
    visited = [[False for _ in range(n)] for __ in range(n)]
    q = deque()
    cnt = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                visited[i][j] = True
                q.append((i,j))

                while q:
                    
                    x, y = q.popleft()

                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]

                        if 0 <= nx < n and 0 <= ny < n:
                            #print(nx,ny)
                            if not visited[nx][ny] and printing[x][y] == printing[nx][ny]:
                                visited[nx][ny] = True
                                q.append((nx,ny))
                cnt += 1
    return cnt

def otherBFS():
    visited = [[False for _ in range(n)] for __ in range(n)]
    q = deque()
    for i in range(n):
        for j in range(n):
            if printing2[i][j] == "R" or printing2[i][j] == "G":
                printing2[i][j] = "A"
    cnt = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                visited[i][j] = True
                q.append((i,j))

                while q:
                    
                    x, y = q.popleft()

                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]

                        if 0 <= nx < n and 0 <= ny < n:
                            #print(nx,ny)
                            if not visited[nx][ny] and printing2[x][y] == printing2[nx][ny]:
                    
                                visited[nx][ny] = True
                                q.append((nx,ny))
                cnt += 1
    return cnt

n = int(input())
printing = [[] for _ in range(n)]
for x in range(n):
    temp = input()
    for t in temp:
        printing[x].append(t)

print(normalBFS())
printing2 = copy.deepcopy(printing)
print(otherBFS())


