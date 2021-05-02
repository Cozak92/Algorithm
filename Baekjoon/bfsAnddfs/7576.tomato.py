from collections import deque

M,N = list(map(int,list(input().split())))
q = deque()
farm = []
dx = [0,0,1,-1]
dy = [1,-1,0,0]
isVisited = [[False for _ in range(M)] for __ in range(N)]
days = 0

for i in range(N):
    farm.append(list(map(int,list(input().split()))))
    for j in range(M):
        if farm[i][j] == 1:
            q.append((i,j))
            isVisited[i][j] = True


while q:

    
    for a in range(len(q)):
        x,y = q.popleft()

        for b in range(4):

            nx = x + dx[b]
            ny = y + dy[b]

            if 0 <= nx < N and 0 <= ny < M and not isVisited[nx][ny]:
                if farm[nx][ny] == 0:
                    farm[nx][ny] = 1
                    isVisited[nx][ny] = True
                    q.append((nx,ny))
    days += 1

    # print("----")
    # for f in farm:
    #     print(f)
flag = True
for check in farm:
    if 0 in check:
        print(-1)
        
        flag = False
        break

if flag : print(days - 1)