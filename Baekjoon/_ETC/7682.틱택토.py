import sys
INF = sys.maxsize
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
MOD = 1000000007
dy = [1, 0, -1, 0]
dx = [0, -1, 0, 1]
dy8 = [1, 1, 0, -1, -1, -1, 0, 1]
dx8 = [0, -1, -1, -1, 0, 1, 1, 1]

def li(): return list(map(int,input().split()))


# def checkWin(target):
#     global board
#     for x in range(3):
#         if board[x][0] == target and board[x][1] == target and board[x][2] == target:
#             return True
#     for y in range(3):
#         if board[0][y] == target and board[1][y] == target and board[2][y] == target:
#             return True
    
#     if board[0][0] == target and board[1][1] == target and board[2][2] == target:
#         return True
#     if board[0][2] == target and board[1][1] == target and board


while 1:
    t = input()  
    if t.startswith("e"): break
    isRowfilled = [[0,0] for _ in range(3)]
    isCoulmnfilled = [[0,0] for _ in range(3)]
    isDiagoanlfileld = [[0,0] for _ in range(2*3)]
    cur = 0
    Xnum = t.count("X")
    Onum = t.count("O")
    board = [[0 for _ in range(4)] for _ in range(4)]

    for i in range(9):
        board[i//3][i%3] = t[i]
        if t[i] == 'X':
            isRowfilled[i//3][0] += 1
            isCoulmnfilled[i%3][0] += 1
            isDiagoanlfileld[2 + i//3 - i%3][0] += 1
        elif t[i] == 'O':
            isRowfilled[i//3][1] += 1
            isCoulmnfilled[i%3][1] += 1
            isDiagoanlfileld[2 + i//3 - i%3][1] += 1

    xWin, oWin = False, False
    for i in range(9):
        if isRowfilled[i//3][0] == 3 or isCoulmnfilled[i%3][0] == 3 or isDiagoanlfileld[2 + i//3 - i%3][0] == 3:
            xWin == True
        if isRowfilled[i//3][1] == 3 or isCoulmnfilled[i%3][1] == 3 or isDiagoanlfileld[2 + i//3 - i%3][1] == 3:
            oWin = True


    if xWin and not oWin and Xnum - Onum == 1:
        print("valid")
    elif not xWin and oWin and Xnum - Onum == 0:
        print("valid")
    elif not xWin and not oWin and Xnum == 5 and Onum ==4:
        print("valid")
    else:
        print("invalid")
       
    



            
    


    

   
    




