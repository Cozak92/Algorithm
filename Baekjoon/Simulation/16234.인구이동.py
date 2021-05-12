from collections import deque
dx = [0,0,1,-1]
dy = [1,-1,0,0]

n, l, r = list(map(int,input().split()))

nations = [list(map(int, input().split())) for _ in range(n)]
isOpen = [[False for _ in range(n)] for __ in range(n)]

q = deque()
ans = 0

for i in range(n):
    for j in range(n):
        isOpen = [[False for _ in range(n)] for __ in range(n)]
        isVisited = [[False for _ in range(n)] for __ in range(n)]
        if not isVisited[i][j]:
            for f in nations:
                print(f)
            q.append((i,j))
            isVisited[i][j] = True
            minNum = nations[i][j]

            while q:
                x,y = q.popleft()

                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]

                    if 0 <= nx < n and 0 <= ny < n and not isVisited[nx][ny]:
                        
                        if l <= abs(minNum - nations[nx][ny]) <= r:
                            minNum = min(minNum,nations[nx][ny])
                            isOpen[x][y] = True                           
                            isOpen[nx][ny] = True

                            isVisited[nx][ny] = True
                            
                            q.append((nx,ny))

            SUM = 0
            cnt = 0
            flag = False
            for a in range(n):
                for b in range(n):
                    if isOpen[a][b]:
                        print(a,b)
                        SUM += nations[a][b]
                        cnt += 1
                        flag = True
            for a in range(n):
                for b in range(n):
                    if isOpen[a][b]:
                        nations[a][b] = SUM // cnt

            if flag: ans += 1
                
            
print(ans)
            


