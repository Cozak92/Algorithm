from collections import deque
import sys

answer = sys.maxsize
dx = [0,0,1,-1]
dy = [1,-1,0,0]
picCnt = 0


n, m = list(map(int,list(input().split())))
pic = [[] for _ in range(n)]
for i in range(n):
    temp = list(input().rstrip())
    for a in range(len(temp)):
        #print(temp[a])
        pic[i].append(int(temp[a]))

q = deque()
isVisited = [[False for _ in range(m)] for __ in range(n)]

q.append((0,0,0))
isVisited[0][0] = True
#print(pic)

while q:

    x,y,size = q.popleft()

    size += 1
    #print(x,y,size)
    if x == n -1 and y == m - 1:
        answer = min(answer,size)


    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < n and 0 <= ny < m and not isVisited[nx][ny]:
            
            if pic[nx][ny] == 1:
                

                q.append((nx,ny,size))                                             
                
  
            isVisited[nx][ny] = True


print(answer)