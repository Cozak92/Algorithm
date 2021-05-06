n, m, x, y, k = list(map(int, input().split()))
board = [list(map(int, input().split())) for _ in range(n)]
dice = [0,0,0,0,0,0]

DIR = [[4,2,1,6,5,3],[3,2,6,1,5,4],[2,6,3,4,1,5],[5,1,3,4,6,2]]

def doRotate(order):
    global DIR
    temp = [0 for _ in range(6)]

    for i in range(6):

        temp[DIR[order][i] - 1] = dice[i]

    for i in range(6):

        dice[i] = temp[i]



order = list(map(int, input().split()))

print(order)
for o in order:
    #print(x,y)

    flag = True

    if(y < m - 1 and o == 1):
        doRotate(o - 1)
        y += 1
    elif(y > 0 and o == 2):
        doRotate(o - 1)
        y -= 1
    elif(x > 0 and o == 3):
        doRotate(o - 1)
        x -= 1
    elif(x < n - 1 and o == 4):
        doRotate(o - 1)
        x += 1
    else: flag = False


    if flag:
        if board[x][y] == 0:
            board[x][y ]= dice[5]
        else:
            dice[5] = board[x][y]
            board[x][y] = 0

        print(dice[0])


    
    

    