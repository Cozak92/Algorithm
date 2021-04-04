import sys

n = int(sys.stdin.readline())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

q = []
m = -1


f = [list(map(int, list(input().split()))) for _ in range(n)]

def bfs(q,j,k):
    q.append([j,k])
    t[j][k] = 1

    while q:


        y, x = q.pop()

                    
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n :
                if v[ny][nx] == 1 and t[ny][nx] == 0 :
                    q.append([ny,nx])
                    t[ny][nx] = 1

t = ([ [0] * n for _ in range(n)])
v = ([ [0] * n for _ in range(n)])
s = 0


for i in range(1,101):


    for j in range(n):
        for k in range(n):
            if f[j][k] > i and t[j][k] == 0:
                v[j][k] = 1
                bfs(q,j,k)
                s += 1

                
                
    m = max(m,s)

print(m)
                


            


