
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

dx = [0,0,1,-1]
dy = [1,-1,0,0]




icebergs = [[ int(x) for x in input().split()] for __ in range(N)]



years = 0
q = []

def bfs(i,j):

    visited[i][j] = True
    
    q.append((i,j))

    while q:

        x,y = q.pop()

        for k in range(4):
            nx = x+dx[k]
            ny = y+dy[k]

                
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:

                if icebergs[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx,ny))
                else:
                    if icebergs[x][y]:
                        icebergs[x][y] -= 1
                            
                            
    


while True:
    chunk = 0
    visited = [[False for _ in range(M)] for __ in range(N)]



    for i in range(N):
        for j in range(M):
            #print(i,j)
            if icebergs[i][j] and not visited[i][j]:
                bfs(i,j)
                chunk += 1

        
    if chunk >= 2:
        print(years)
        break
    elif chunk == 0:
        print(chunk)
        break
    
    # count = 0
    # for i in range(N):
    #     for j in range(M):
            
    #         icebergs[i][j] = 0 if icebergs[i][j] - warter[i][j] <= 0 else icebergs[i][j] - warter[i][j]

    #         if not icebergs[i][j]:
    #             count +=1
            
        
    # if count == N*M:
    #     print(0)
    #     break
    #for i in range(N):
    #    print(icebergs[i],"\n")
    years += 1



                    

                        
                        