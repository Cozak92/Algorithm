# (0,0)에 상어가 들어온다.
# 각각의 방향을 딕셔너리로 좌표를 저장해둔다.
# shark = [x,y]
# 상어가 움직이고 물고기들이 움직인다.

# dfs 갈수잇는 모든 칸을 들어간다.

# dfs(상어,방향):
#  물고기들이 움직임( 움직일수 없다면(벽이거나 상어가 있거나) 방향을 반시계로 45도씩 돌린다.)
# 상어가 갈수있는 방향 체크!
# 물고기 있따면 다 들어가봄
# 그중 최대값만 가져옴
# 리턴
# 

import copy

def hunting(shark,where,scores,seas,fishess):
    
    sea = copy.deepcopy(seas)
    fishes = copy.deepcopy(fishess)
    print("shark = ",shark)
    print("where = ", where)
    
    sx, sy = shark
    del fishes[sea[sx][sy]]
    sea[sx][sy] = 0
    #print(direction)
    #print(where)
    sdx, sdy = direction[where]
    snx, sny = sx + sdx, sy + sdy
  
    

 
        

    for fish in fishes:
        for x in range(4):
            for y in range(4):
                if sea[x][y] == fish:
                    #print(x,y,fish)

                    dx, dy = direction[fishes[fish]]
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < 4 and 0 <= ny < 4 and (sx != nx and sy != ny): #움직일수 있으면 바로 반시계
                        temp = sea[nx][ny]
                        sea[nx][ny] = sea[x][y]
                        sea[x][y] = temp
                    else: #벽이거나 상어가 있거나 움직일 수 있을때까지 반시계
                        for k in range(1,8):
                            #print(k)
                            if fishes[fish]+k >= 8:
                                target = (fishes[fish]+k) % 8 + 1
                            else:
                                target = fishes[fish]+k

                            dx, dy = direction[target]
                            nx, ny = x + dx, y + dy

                            if 0 <= nx < 4 and 0 <= ny < 4 and (sx != nx and sy != ny):
                                temp = sea[nx][ny]
                                sea[nx][ny] = sea[x][y]
                                sea[x][y] = temp
                                fishes[fish] = target
                                break
    while 0 <= snx < 4 and 0 <= sny < 4:
        fish = sea[snx][sny]
        if fish != 0: #고기가 있을때만 움직일수잇음
            score = hunting([snx,sny],fishes[fish],scores + fish,sea,fishes)
            if score > scores:
                scores = score
                print(fish)
                print("냠")
                print(score)
                
        snx += sdx
        sny += sdy
        
    return scores
   


direction = {1:[-1,0], 2 : [-1,-1], 3: [0,-1], 4:[1,-1],5:[1,0],6:[1,1],7:[0,1],8:[-1,1]}
fishes = {}
sea = [[0 for __ in range(4)] for _ in range(4)]

print(sea)

for i in range(4):
    row = list(map(int, list(input().split())))

    for j in range(0,8,2):
        print(i,j//2)
        sea[i][j//2] = row[j]
        fishes[row[j]] = row[j+1]



fishes = sorted(fishes.items())
fishes = dict(fishes)
shark = [0,0]

print(sea)
print(fishes)

answer = hunting(shark,fishes[sea[0][0]],0,sea,fishes)
print(answer)
print(sea)
print(fishes)
    