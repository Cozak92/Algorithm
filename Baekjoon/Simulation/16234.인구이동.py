from collections import deque
dx = [0,0,1,-1]
dy = [1,-1,0,0]
def bfs():
    q = deque()
    isVisited = [[False for _ in range(n)] for __ in range(n)]
    flag = False
    for i in range(n):
        for j in range(n):        
            if not isVisited[i][j]:
                sum = nations[i][j]
                stack = []
                q.append((i,j))
                stack.append((i,j))
                isVisited[i][j] = True

                while q:
                    x,y = q.popleft()

                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]

                        if 0 <= nx < n and 0 <= ny < n and not isVisited[nx][ny]:
                            
                            if l <= abs(nations[x][y] - nations[nx][ny]) <= r:

                                sum += nations[nx][ny]
                                isVisited[nx][ny] = True
                                stack.append((nx,ny))
                                q.append((nx,ny))

                if len(stack) >= 2:
                    avg = sum // len(stack)
                    flag= True
                    for a,b in stack:
                        nations[a][b] = avg


    return flag

n, l, r = list(map(int,input().split()))

nations = [list(map(int, input().split())) for _ in range(n)]
isOpen = [[False for _ in range(n)] for __ in range(n)]


ans = 0
while True:
    flag = bfs()
    if flag:
        ans += 1
    else: break
print(ans)
            


