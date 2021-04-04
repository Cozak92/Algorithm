from itertools import combinations
 
## 맵크기(N), 치킨집 최대 선택가능개수(M)
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
 
## 빈칸(0), 집(1), 치킨집(2)
house = []
chicken = []
for i in range(N):
    for j in range(N):
        if board[i][j] == 1: house.append((i, j))
        elif board[i][j] == 2: chicken.append((i, j))
 
minv = float('inf')
for ch in combinations(chicken, M):
    sumv = 0
    for home in house:
        sumv += min([abs(home[0]-i[0])+abs(home[1]-i[1]) for i in ch])
        if minv <= sumv: break
    if sumv < minv: minv = sumv
 
print(minv)


            
