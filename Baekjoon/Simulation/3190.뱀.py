from collections import deque


def movable(x,y):
    if 0 <= x < n and 0 <= y < n and (x, y) not in snake:
        return True
    else: return False

def changeDir(s):
    global headDir
    if s == "L":
        headDir = (headDir-1) % 4
    else:
        headDir = (headDir+1) % 4

#######입력처리#####
snake = deque()
n = int(input())
k = int(input())
dir = {0 : (0,1), 1:(1,0), 2:(0,-1), 3:(-1,0)}
orderTable = {}
board = [[0 for _ in range(n)] for __ in range(n)]

for _ in range(k):
    x,y = list(map(int,list(input().split())))
    board[x-1][y-1] = 1
l = int(input())
for _ in range(l):
    nextSec, order =list(input().split())
    orderTable[int(nextSec)] = order
####################
headDir = 0
leng = 1
x,y = 0,0
dx, dy = dir[headDir]
snake.append((0,0))

for curTime in range(1,100000):
    x += dx
    y += dy
    
    if not movable(x,y):
        break

    snake.append((x,y))

    if board[x][y] == 1:
        leng += 1
        board[x][y] = 0
    else:
        if len(snake) > leng:
            snake.popleft()
    if orderTable.get(curTime):
        order = orderTable.get(curTime)
        changeDir(order)
        dx, dy = dir[headDir]
    

print(curTime)
