from collections import deque

north = [0,0,0,0]
east = [0,0,0]
# north index 2 = east index 2
# if move to south - 
# t = north.pop()
# north.appendleft(t)
# east[1] = north[1]
# north[-1] // bottom
# north[0] // top

# if move to north
# t = north.popleft()
# north.append(t)
# east[1] = north[1]
# north[0] // bottom
# north[-1] // top
north = deque([0,0,0,0])
east = deque([0,0,0])

n, m, x, y, k = list(map(int, input().split()))
board = [list(map(int, input().split())) for _ in range(n)]
order = list(map(int, input().split()))
print(order)
for o in order:
    print(north,east)
    if o == 1:
        if y + 1 >= m:
            continue
        print(east[-1])
        y += 1
        t = east.popleft()
        east.append(t)
        north[1] = east[1] 
        if board[x][y] == 0:
            board[x][y] = east[1] 
        else:
            east[1] = board[x][y]
            board[x][y] = 0
        
        
            
    if o == 2:
        if y - 1 < 0:
            continue
        y -= 1
        print(east[0])
        t = east.pop()
        east.appendleft(t)
        north[1] = east[1] 
        if board[x][y] == 0:
            board[x][y] = east[1] 
        else:
            east[1] = board[x][y]
            board[x][y] = 0
        
        
    if o == 3:
        if x - 1 < 0:
            continue
        print(north[-2])
        x -= 1
        t = north.popleft()
        north.append(t)
        east[1] = north[1]
        if board[x][y] == 0:
            board[x][y] = north[1] 
        else:
            north[1] = board[x][y]
            board[x][y] = 0
        
        

    if o == 4:
        if x + 1 >= n:
            continue
        print(north[0])
        x += 1
        t = north.pop()
        north.appendleft(t)
        
        if board[x][y] == 0:
            board[x][y] = north[1] 
        else:
            north[1] = board[x][y]
            board[x][y] = 0
        east[1] = north[1]
        
    