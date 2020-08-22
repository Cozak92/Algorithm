#백준 7576

# dx[0] dy[0] = 왼
# dx[1] dy[1] = 오
# dx[2] dy[2] = 위
# dx[3] dy[3] = 아래


dx = [-1, 1, 0 , 0]
dy = [0, 0, 1, -1]

M , N = map(int, input().split())


matrix = [list(map(int, list(input().split()))) for _ in range(N)]


visit = [[False]* M for i in range(N)]
queue = []
tomatoes = M * N
ripeNum =0
rottenNum =0
daysNum = {} #자신이 며칠쨰에 익었는지



def bfs():
    global ripeNum

    while len(queue) != 0:
                ax, ay = queue.pop(0)

                for i in range(4):
                    nx, ny = ax+dx[i], ay+dy[i]
                    
                    if 0 <= nx < N and 0 <= ny < M:
                        if matrix[nx][ny] == 0 and visit[nx][ny] == False:
                            daysNum.update({(nx,ny) : daysNum.get((ax,ay)) + 1})                       
                            visit[nx][ny] = True
                            queue.append((nx,ny))
                            ripeNum += 1




for x in range(N):
    for y in range(M):
        if matrix[x][y] == 1 and visit[x][y] == False:
            rottenNum += 1
            visit[x][y] = True
            daysNum.update({(x,y) : 0})
            queue.append((x,y))

        
        

        elif matrix[x][y] == -1:
            rottenNum += 1;

bfs()
            
if (tomatoes - (rottenNum+ripeNum) != 0):
    
    print(-1)
else:
    result = list(daysNum.values())
    print(result[len(result)-1])




