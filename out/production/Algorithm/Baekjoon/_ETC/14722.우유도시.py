from collections import deque
import sys

def dfs(x,y,nxt):
    #print(x,y,nxt)
    if 0 < x < n and 0 < y < n:
        return 0
    if dp[(nxt+1) % 3][x][y] != -1:
        return dp[(nxt+1) % 3][x][y]
    for i in range(2):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < n:
            if city[nx][ny] == (nxt + 1) % 3:
                dp[nxt][x][y] = max(dp[nxt][x][y], dfs(nx,ny,(nxt + 1) % 3) + 1)
            dp[nxt][x][y] = max(dp[nxt][x][y],dfs(nx,ny,nxt))
    return dp[nxt][x][y]

answer = -sys.maxsize
n = int(input())

dx = [0,1]
dy = [1,0]
dp =[[[-1 for _ in range(n)] for __ in range(n)] for ___ in range(3)]

city = []
for i in range(n):
    city.append(list(map(int,list(input().split()))))

if city[0][0] == 0 : print(dfs(0, 0, 0) + 1)
else: print(dfs(0, 0, -1))

# q = deque()
# q.append(((0,0),1,0))


# while q:
#     pos, drink, num = q.popleft()
#     x,y = pos

#     print(pos,drink,num)
#     for i in range(2):
#         nx = x + dx[i]
#         ny = y + dy[i]

#         if 0 <= nx < n and 0 <= ny < n:
#             if not isVisited[nx][ny]:
#                 isVisited[nx][ny] = True
#                 if city[nx][ny] == drink:
#                     answer = max(answer,num + 1)
#                     q.append(((nx,ny),(drink+1)%3,num + 1))
#                 else:
#                     q.append(((nx,ny),drink,num))
                    

    

