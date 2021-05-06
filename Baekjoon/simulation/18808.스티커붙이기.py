import copy

n, m, k = list(map(int, input().split()))
note = [[0 for _ in range(m)] for __ in range(n)]
def attachable(x,y):
    
    #print(x,y)
    for i in range(r):
        for j in range(c):
            if note[x+i][y+j] == 1 and sticker[i][j] == 1:
                return False
    
    return True

def doAttach(x,y):

    for i in range(r):
        for j in range(c):
   
            if sticker[i][j] == 1:
                note[x+i][y+j] = 1

def doRotate():
    global r,c,sticker
    temp = [[0 for _ in range(r)] for __ in range(c)]
  

    for i in range(c):
        for j in range(r):
            temp[i][j] = sticker[r - 1 - j][i]
    
    sticker = copy.deepcopy(temp)
    r, c = c, r    

for i in range(k):

    r, c = list(map(int, input().split()))
    sticker = [list(map(int, input().split())) for _ in range(r)]

    for rot in range(4):
        isAttachable = False
        for x in range(n-r+1):
            if isAttachable: break
            for y in range(m-c+1):
                
                if attachable(x,y):
                    
                    isAttachable = True
                    doAttach(x,y)
                    break
        if isAttachable: break
        doRotate()

ans = 0
for i in range(n):
    for j in range(m):
        ans += note[i][j]


print(ans)
