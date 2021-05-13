# from collections import deque
# import copy

# growing = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
# n,m,k = list(map(int,input().split()))

# S2D2 = [0] + [[0] + list(map(int,input().split())) for _ in range(n)]
# # trees = [list(map(int,input().split())) for _ in range(m)]
# trees = deque()
# for i in range(m):
#     x, y, z = list(map(int, input().split()))
#     trees.append((x,y,z))
# field = [[0 for _ in range(n+1)] for __ in range(n+1)]
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         field[i][j] = 5
# year = 0
# # print(trees)
# # for f in field:
# #     print(f)
# # print("###################")
# while trees and year < k:
#     trees = sorted(trees, key = lambda x : x[2])
#     trees= deque(trees)
#     # print(trees)
#     # for f in field:
#     #     print(f)
#     # print("###################")

#     year += 1
#     deads = []
#     #봄
#     v = len(trees)
#     for _ in range(v):
#         x,y,z = trees.popleft()
#         if field[x][y] - z >= 0:
#             field[x][y] -= z
#             trees.append((x,y,z+1))
#         else:
#             deads.append((x,y,z))
#     #여름


    
#     for dead in deads:
#         x,y,z = dead
#         field[x][y] += z//2
#     #가을
#     cnt = 0
#     trees = list(trees)
#     for tree in trees:
        
#         x,y,z = tree
#         if not z % 5:
#             cnt += 1
#             for i in range(8):
#                 dx,dy = growing[i]
#                 nx = x + dx
#                 ny = y + dy

#                 if 1 <= nx < n+1 and 1 <= ny < n+1:
#                     trees.append((nx,ny,1))
                    
#     #겨울
#     for a in range(1,n+1):
#         for b in range(1,n+1):
#             field[a][b] += S2D2[a][b]
#     # for f in field:
#     #     print(f)
#     # print("###################")

# print(len(trees))


from collections import deque
import sys
input = sys.stdin.readline
def spring():
    for i in range(n):
        for j in range(n):
            len_t = len(t[i][j])
            for k in range(len_t):
                if t[i][j][k] <= no[i][j]:
                    no[i][j] -= t[i][j][k]
                    t[i][j][k] += 1
                else:
                    for _ in range(k, len_t):
                        no[i][j] += t[i][j].pop() // 2
                    break
def fall():
    for i in range(n):
        for j in range(n):
            for k in t[i][j]:
                if k % 5 == 0:
                    for l in range(8):
                        x = i + dx[l]
                        y = j + dy[l]
                        if 0 <= x < n and 0 <= y < n:
                            t[x][y].appendleft(1)
            no[i][j] += s[i][j]
dx = [1, -1, 0, 0, 1, -1, 1, -1]
dy = [0, 0, -1, 1, 1, -1, -1, 1]
n, m, k = map(int, input().split())
s = []
t = [[deque() for i in range(n)] for i in range(n)]
no = [[5] * n for i in range(n)]
for i in range(n):
    s.append(list(map(int, input().split())))
for i in range(m):
    x, y, z = map(int, input().split())
    t[x - 1][y - 1].append(z)
for i in range(k):
    spring()
    fall()
cnt = 0
for i in range(n):
    for j in range(n):
        cnt += len(t[i][j])
print(cnt)