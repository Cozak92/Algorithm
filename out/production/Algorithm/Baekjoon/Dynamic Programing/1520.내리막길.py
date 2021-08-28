import sys

input = sys.stdin.readline
dir = [[0,-1],[0,1],[-1,0],[1,0]]

def dfs(x,y):
    if x == column - 1 and y == row - 1:
        return 1

    if dp[x][y] != -1: 
        return dp[x][y]
    dp[x][y] = 0
    for dx,dy in dir:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < column and 0 <= ny < row:
            if board[x][y] > board[nx][ny]:
                dp[x][y] += dfs(nx,ny)
    return dp[x][y]
                

column, row = list(map(int,input().split()))
board = [list(map(int,input().split())) for _ in range(column)]
dp = [[-1] * row for __ in range(column)]

print(dfs(0,0))


# import sys

# input = sys.stdin.readline
# dx = [1, -1, 0, 0]
# dy = [0, 0, 1, -1]

# def dfs(x, y):
#     if x == m-1 and y == n-1:
#         return 1
#     if c[x][y] != -1:
#         return c[x][y]
#     c[x][y] = 0
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if 0 <= nx < m and 0 <= ny < n:
#             if a[nx][ny] < a[x][y]:
#                 c[x][y] += dfs(nx, ny)
#     return c[x][y]

# m, n = map(int, input().split())
# a = [list(map(int, input().split())) for _ in range(m)]
# c = [[-1]*n for _ in range(m)]
# print(dfs(0, 0))












# for x in range(column):
#     for y in range(row):
#         print(x,y)
        
#         print("--------------")
#         for dx,dy in dir:
#             nx = x + dx
#             ny = y + dy

#             if 0 <= nx < column and 0 <= ny < row:
#                 if board[x][y] < board[nx][ny]:
#                     dp[x][y] += dp[nx][ny]

# print(dp[column-1][row-1])


# path = deque()
# path.append((0,0))
ans = 0
# while path:

#     x, y = path.popleft()
#     if x == column - 1 and y == row - 1:
#         ans += 1
#         continue
#     for dx,dy in dir:
#         nx = x + dx
#         ny = y + dy

#         if 0 <= nx < column and 0 <= ny < row:
#             if board[x][y] > board[nx][ny]:
#                 path.append((nx,ny))

# print(ans)
