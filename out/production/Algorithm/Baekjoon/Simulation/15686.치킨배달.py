from itertools import combinations
import sys

n, m = list(map(int, input().split()))
city = [list(map(int,input().split())) for _ in range(n)]
house = []
chiken = []

for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            house.append((i,j))
        if city[i][j] == 2:
            chiken.append((i,j))

chikenN = len(chiken)
ans = sys.maxsize

dp = [[0,0] for _ in range(chikenN)]

def findDist(cx,cy):

    for i in range(len(house)):
        x,y = house[i]
        tmp = abs(cx-x) + abs(cy-y)
        dist[i] = min(dist[i],tmp)

for item in combinations(chiken,m):
    dist = [2*n for _ in range(len(house))]
    for x,y in item:
        findDist(x,y)
    ans = min(ans,sum(dist))
print(ans)
        
    
    
