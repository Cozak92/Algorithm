import copy
from collections import Counter
dx = [1,0,-1,0]
dy = [0,1,0,-1]


n, m = list(map(int, input().split()))
cctv = []
room = []
romm2 = []
ans = 0
for i in range(n):
    temp = list(map(int,input().split()))
    room.append(temp)
    for j in range(m):
        if room[i][j] != 6 and room[i][j] != 0:
            cctv.append((i,j))
        else:
            ans += 1
def upd(x,y,Dir):
    Dir = Dir % 4
    while 1:
        x += dx[Dir]
        y += dy[Dir]
        if 0 <= x < n and 0 <= y < m:
            if room2[x][y] == 6:
                return
            if room2[x][y] != 0:
                continue
            room2[x][y] = 7
        else: return
# print(cctv)
num = len(cctv)

for temp in range(1<<(2*num)):
    room2 = copy.deepcopy(room)
    brute = temp

    for i in range(num):
        Dir = brute % 4
        brute = brute // 4
        x,y = cctv[i]

        if room[x][y] == 1:
            upd(x,y,Dir)
        elif room[x][y] == 2:
            upd(x,y,Dir)
            upd(x,y,Dir + 2)
        elif room[x][y] == 3:
            upd(x,y,Dir)
            upd(x,y,Dir + 1)
        elif room[x][y] == 4:
            upd(x,y,Dir)
            upd(x,y,Dir + 1)
            upd(x,y,Dir + 2)
        elif room[x][y] == 5:
            upd(x,y,Dir)
            upd(x,y,Dir + 1)
            upd(x,y,Dir + 2)
            upd(x,y,Dir + 3)     

    val = 0
    for r in room2:
        val += Counter(r)[0]
    ans = min(ans,val)  

print(ans)