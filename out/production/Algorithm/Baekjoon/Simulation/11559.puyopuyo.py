from collections import deque

board = [[] for _ in range(12)]
dx = [0,0,-1,1]
dy = [1,-1,0,0]
ans = 0

def destoryPuyo(stack):

    stack = sorted(stack, reverse=True, key= lambda x : x[1])
    for x,y in stack:
        for nx in range(x,0,-1):
            board[nx][y] = board[nx - 1][y]
        board[0][y] = "."


def bfs():
    global ans
    flag = False
    visited =[[False for _ in range(6)] for __ in range(12)]
    q = deque()
    
    for i in range(12):
        for j in range(6):
            if board[i][j] != "." and not visited[i][j]:
                q.append((i,j))
                stack = []
                visited[i][j] = True
                stack.append((i,j))
                while q:

                    x, y = q.popleft()

                    for k in range(4):

                        nx = x + dx[k]
                        ny = y + dy[k]

                        if 0 <= nx < 12 and 0 <= ny < 6:
                            if not visited[nx][ny] and board[nx][ny] == board[x][y]:
                                q.append((nx,ny))
                                visited[nx][ny] = True
                                stack.append((nx,ny))
                               

                if len(stack) >= 4:
                    flag = True
                    destoryPuyo(stack)
    return flag
    
                

for i in range(12):
    temp = input()
    for t in temp:
        board[i].append(t)


while 1:
    
    ret = bfs()
    if ret:
        ans += 1
    else:
        break

print(ans)
