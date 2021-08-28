from collections import deque
from itertools import combinations

dx = [0,0,-1,1]
dy = [1,-1,0,0]
ans = 0
n = 5
classRoom = [[] for _ in range(n)]
candidate = [x for x in range(25)]
for i in range(n):
    row = input()
    for r in row:
        classRoom[i].append(r)

def findAdj(item):
    visit = [[False for _ in range(n)] for __ in range(n)]
    q = deque()
    q.append((item[0]//5,item[0]%5))
    visit[item[0]//5][item[0]%5] = True
    cnt = 1

    while q:

        x,y = q.popleft()
        if cnt == 7:
            return True
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < 5 and 0 <= ny < 5:
                if not visit[nx][ny] and (nx*5 + ny) in item:
                    visit[nx][ny] = True
                    cnt += 1
                    q.append((nx,ny))
    
    return False


for item in combinations(candidate,7):
    cnt = 0
    for n in item:
        if classRoom[n//5][n%5] == "S":
            cnt += 1
    if cnt >= 4:
        if findAdj(item):
            ans += 1

print(ans)



# for i in range(n):
#     for j in range(n):
#         temp = classRoom[i][j]
#         q = deque()
#         stack = []
#         q.append((i,j,temp))
#         visit = [[False for _ in range(n)] for __ in range(n)]

        
        
#         while q:
            
#             x,y,temp = q.popleft()
#             if len(temp) == 6:
#                 t = temp.count("S")
#                 if t >= 4:
#                     print(stack)
#                     print(temp)
#                     ans +=1
#                 continue

#             for k in range(4):
#                 nx = x + dx[k]
#                 ny = y + dy[k]

#                 if 0 <= nx < n and 0 <= ny < n:
#                     if not visit[nx][ny]:
#                         visit[nx][ny] = True
#                         temp += classRoom[nx][ny]
#                         q.append((nx,ny,temp))


        
