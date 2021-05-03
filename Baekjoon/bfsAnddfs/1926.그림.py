from collections import deque
import sys

answer = -sys.maxsize
dx = [0,0,1,-1]
dy = [1,-1,0,0]
picCnt = 0
size = 0

n, m = list(map(int,list(input().split())))
pic = []
for i in range(n):
    pic.append(list(map(int,list(input().split()))))

q = deque()
isVisited = [[False for _ in range(m)] for __ in range(n)]

for k in range(n):
    for j in range(m):


        if pic[k][j] == 1 and not isVisited[k][j]:
            isVisited[k][j] = True
            q.append((k,j))
            size = 0
            picCnt  += 1

        while q:

            x,y = q.popleft()
            size += 1

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if 0 <= nx < n and 0 <= ny < m and not isVisited[nx][ny]:
                    
                    if pic[nx][ny] == 1:

                        q.append((nx,ny))                                             
                        isVisited[nx][ny] = True
        answer = max(size,answer)

print(picCnt,answer)

    