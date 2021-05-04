import heapq
import sys

INF = sys.maxsize
dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(x,y):
    q = []
    isVisited = [[False for _ in range(n)] for __ in range(n)]
    lost[x][y] = cave[x][y]
    heapq.heappush(q,(lost[x][y],x,y))
    
    isVisited[x][y] = True

    while q:

        curLost, curX,curY = heapq.heappop(q)


        for i in range(4):
            nextX = curX + dx[i]
            nextY = curY + dy[i]

            if 0 <= nextX < n and 0 <= nextY < n and not isVisited[nextX][nextY]:
                nextLost = cave[nextX][nextY]
                if curLost + nextLost < lost[nextX][nextY]:
                    lost[nextX][nextY] = curLost + nextLost
                    heapq.heappush(q,(lost[nextX][nextY],nextX,nextY))
                    isVisited[nextX][nextY] = True



i = 1
while 1:
    n = int(input())
    if n == 0:
        break
    cave = [list(map(int,input().split())) for _ in range(n)]
    lost = [[ INF for _ in range(n)] for __ in range(n)]
   
    bfs(0,0)

    print("Problem",str(i)+":",lost[n-1][n-1])
    i += 1