import sys
from collections import Counter
INF = sys.maxsize
# 0번째 카메라.... ?
# 입력을 받을때 각각 카메라의 위치를 저장하자
# 회전을 어떻게 처리해야하지?

def rightFunc(x,y,fill,k):
     for j in range(y+1,m):
        if room[x][j] == 6:
            break
        if room[x][j] not in (0,-1):
            continue
        if fill:
            if ID[x][j] == -1:
                ID[x][j] = k
            room[x][j] = fill
        else:
            if ID[x][j] == k:
                room[x][yj] = fill


def leftFunc(x,y,fill,k):
    for j in range(y-1,-1,-1):
        if room[x][j] == 6:
            break
        if room[x][j] not in (0,-1):
            continue
        if fill:
            if ID[x][j] == -1:
                ID[x][j] = k
            room[x][j] = fill
        else:
            if ID[x][j] == k:
                room[x][j] = fill


def downFunc(x,y,fill,k):
    for j in range(x+1,n):
        if room[j][y] == 6:
            break
        if room[j][y] not in (0,-1):
            continue
        if fill:
            if ID[j][y] == -1:
                ID[j][y] = k
            room[j][y] = fill
        else:
            if ID[j][y] == k:
                room[j][y] = fill


def topFunc(x,y,fill,k):
    for j in range(x-1,-1,-1):
        if room[j][y] == 6:
            break
        if room[j][y] not in (0,-1):
            continue
        
        if fill:
            if ID[j][y] == -1:
                ID[j][y] = k
            room[j][y] = fill
        else:
            if ID[j][y] == k:
                room[j][y] = fill



# n = column , m = row
def func(k):
    global ans
    print("-------", k)
    for l in room:
        print(l)

    # base condition
    if k == num:
        # print("-------")
        # for l in room:
        #     print(l)
        temp = 0
        for r in room:
            temp += Counter(r)[0]
        ans = min(ans,temp)
        return
    x,y = cctv[k]
    
    for i in range(4):
        # 1 = 오른쪽,아래,왼쪽,위
        if room[x][y] == 1:
            if i == 0:
                leftFunc(x,y,-1,k)
                func(k+1)
                leftFunc(x,y,0,k)

            elif i == 1:
                downFunc(x,y,-1,k)
                func(k+1)
                downFunc(x,y,0,k)

            elif i == 2:
                
                rightFunc(x,y,-1,k)
                func(k+1)
                rightFunc(x,y,0,k)
            elif i == 3:
                topFunc(x,y,-1,k)
                func(k+1)
                topFunc(x,y,0,k)
        # 2 = x행, y열
        if room[x][y] == 2:
            if i % 2 == 0:
              leftFunc(x,y,-1,k)
              rightFunc(x,y,-1,k)
              func(k+1)
              leftFunc(x,y,0,k)
              rightFunc(x,y,0,k)

            elif i % 2 == 1:
                topFunc(x,y,-1,k)
                downFunc(x,y,-1,k)
                func(k+1)
                topFunc(x,y,0,k)
                downFunc(x,y,0,k)
               
        # 3 =
        if room[x][y] == 3:
            if i == 0:
                topFunc(x,y,-1,k)
                rightFunc(x,y,-1,k)
                func(k+1)
                topFunc(x,y,0,k)
                rightFunc(x,y,0,k)

            elif i == 1:
                rightFunc(x,y,-1,k)
                downFunc(x,y,-1,k)
                func(k+1)
                rightFunc(x,y,0,k)
                downFunc(x,y,0,k)


            elif i == 2:
                downFunc(x,y,-1,k)
                leftFunc(x,y,-1,k)
                func(k+1)
                downFunc(x,y,0,k)
                leftFunc(x,y,0,k)

            elif i == 3:
                leftFunc(x,y,-1,k)
                topFunc(x,y,-1,k)
                func(k+1)
                leftFunc(x,y,0,k)
                topFunc(x,y,0,k)
        # 4 = (왼,위,오), (위,오,아래), (오,아래,왼), (아래,왼,위)
        if room[x][y] == 4:
            if i == 0:
                leftFunc(x,y,-1,k)
                topFunc(x,y,-1,k)
                rightFunc(x,y,-1,k)
                func(k+1)
                leftFunc(x,y,0,k)
                topFunc(x,y,0,k)
                rightFunc(x,y,0,k)

                
            elif i == 1:
                downFunc(x,y,-1,k)
                topFunc(x,y,-1,k)
                rightFunc(x,y,-1,k)
                func(k+1)
                downFunc(x,y,0,k)
                topFunc(x,y,0,k)
                rightFunc(x,y,0,k)
            elif i == 2:
                leftFunc(x,y,-1,k)
                downFunc(x,y,-1,k)
                rightFunc(x,y,-1,k)
                func(k+1)
                leftFunc(x,y,0,k)
                downFunc(x,y,0,k)
                rightFunc(x,y,0,k)
            elif i == 3:
                leftFunc(x,y,-1,k)
                downFunc(x,y,-1,k)
                topFunc(x,y,-1,k)
                func(k+1)
                leftFunc(x,y,0,k)
                downFunc(x,y,0,k)
                topFunc(x,y,0,k)
        if room[x][y] == 5:
            rightFunc(x,y,-1,k)
            leftFunc(x,y,-1,k)
            downFunc(x,y,-1,k)
            topFunc(x,y,-1,k)
            func(k+1)
            rightFunc(x,y,0,k)
            leftFunc(x,y,0,k)
            downFunc(x,y,0,k)
            topFunc(x,y,0,k)
        


n, m = list(map(int, input().split()))
ID = [[-1 for _ in range(m)] for __ in range(n)]
cctv = []
room = []
ans = INF
for i in range(n):
    temp = list(map(int,input().split()))
    room.append(temp)
    for j in range(m):
        if room[i][j] != 6 and room[i][j] != 0:
            cctv.append((i,j))

# print(cctv)
num = len(cctv)

func(0)
print(ans)