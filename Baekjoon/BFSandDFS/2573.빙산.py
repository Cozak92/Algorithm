import sys
from collections import defaultdict
from collections import deque

input = sys.stdin.readline
dx = [0,0,1,-1]
dy = [1,-1,0,0]


n,m = list(map(int,list(input().split())))
pole = [list(map(int,list(input().split()))) for _ in range(n)]


def findCon():
    visited = [[False for _ in range(m)] for _ in range(n)]
    q = deque()
    warter = defaultdict(int)
    con = 0
    # for a in pole:
    #     print(a)
    for i in range(n):
        for j in range(m):
            if pole[i][j] != 0 and not visited[i][j]:
                q.append((i,j))
                visited[i][j] = True
                while q:
                    
                    x,y = q.popleft()
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]

                        if 0 <= nx < n and 0 <= ny < m:
                            if not visited[nx][ny] and pole[nx][ny]:
                                q.append((nx,ny))
                                visited[nx][ny] = True
                            elif not pole[nx][ny]:
                                warter[(x,y)] += 1
                con += 1
                
    #             print(con)
    # print(warter)
    for pos in warter:
        w = warter[pos]
        x, y = pos
        pole[x][y] = pole[x][y] - w if pole[x][y] - w >= 0 else 0

    return con

year = 0
while 1:
    t = findCon()
    if  t >= 2:
        break
    elif t == 0:
        year = 0
        break
    year += 1

print(year)
# def meltIce():
#     q = deque()
#     for i in range(n):
#         for j in range(m):
#             if pole[i][j] != 0:
#                 q.app
#                 for k in range(4):
#                         nx = i + dx[k]
#                         ny = j + dy[k]
#                         if 0 <= nx < n and 0 <= ny < n:
#                             if pole[nx][ny] == 0:
#                                 cnt += 1
                        











