# import sys
# from collections import deque
# INF = sys.maxsize
# input = sys.stdin.readline
# sys.setrecursionlimit(10**6)
# dir = [[0,1],[0,-1],[1,0],[-1,0]]

# def li(): return list(map(int,input().split()))

# def dfs(x,y,cnt):
#     global ans
#     ans = max(cnt,ans)
    
#     for dx,dy in dir:
#         nx = x + dx
#         ny = y + dy
#         if 0 <= nx < r and 0 <= ny < c and not alpha[ord(board[nx][ny]) - 65]:
#             alpha[ord(board[nx][ny]) - 65] = 1
#             dfs(x, y, cnt+1) 
#             alpha[ord(board[nx][ny]) - 65] = 0




# r, c = li()
# board = [[] for _ in range(r)]
# for i in range(r):
#     temp = input()
#     for t in temp:
#         board[i].append(t)


# alpha = [0] * 27
# alpha[ord(board[0][0]) - 65] = 1
# ans = -1

# dfs(0,0,1)
# print(ans)
# while q:

#     x,y,cnt,cache = q.popleft()
#     ans = max(cnt,ans)
    
#     for dx,dy in dir:
#         nx = x + dx
#         ny = y + dy
#         if 0 <= nx < r and 0 <= ny < c:
#             if not cache & 1 << ord(board[nx][ny]) - ord("A"):
#                 nextCache = 1 << (ord(board[nx][ny]) - ord("A"))
#                 q.append((nx,ny,cnt+1,nextCache | cache))


def solve(x, y, l): 
    global ans 
    ans = max(ans, l) 
    for d in range(4): 
        i, j = x + dx[d], y + dy[d] 
        if 0<=i<r and 0<=j<c and alpha[table[i][j]] == 0: 
            alpha[table[i][j]] = 1 
            solve(i, j, l+1) 
            alpha[table[i][j]] = 0 
            
r, c = map(int, input().split()) 
table = [list(map(lambda x: ord(x)-65, input().rstrip())) for _ in range(r)] 
dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1) 
alpha = [0] * 26 
ans = 0 
alpha[table[0][0]] = 1 
solve(0, 0, 1) 
print(ans)

