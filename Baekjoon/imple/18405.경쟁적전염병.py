from collections import deque


def bfs(q):

    while q:

        curVirus, curPos, curTime = q.popleft()

        x, y = curPos

        if curTime == s:
            break

    
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0<= ny < n:
                if matrix[nx][ny] == 0:
                    matrix[nx][ny] = curVirus
                    q.append((curVirus,(nx,ny),curTime + 1))
    



n, k = list(map(int,list(input().split())))

matrix =[]
isVisited = [[False for _ in range(n)] for __ in range(n)]
q = deque()
dx = [0,0,1,-1]
dy = [1,-1,0,0]

for i in range(n):
    matrix.append(list(map(int,list(input().split()))))
    for j in range(n):
        if matrix[i][j] != 0:
            q.append((matrix[i][j],(i,j),0))

s,a,b = list(map(int,list(input().split())))

q = sorted(q)
q =deque(q)
bfs(q)

print(matrix[a-1][b-1])


