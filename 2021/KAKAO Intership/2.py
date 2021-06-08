from collections import deque
dx =[0,0,1,-1]
dy = [1,-1,0,0]
def bfs(q,isVisited,room):

    while q:
        
        orix,oriy,x,y,dist = q.popleft()
        # print(orix,oriy)
        if dist >= 2:
            continue
        
        for i in range(4):
            #print(x,y)
            nx = x + dx[i]
            ny = y + dy[i]
           

            if 0 <= nx < 5 and 0 <= ny < 5 and room[nx][ny] != "X":
                if room[nx][ny] == "P" and (nx != orix or ny != oriy):
                    # print(room[nx][ny])
                    # print("NX,NY", nx,ny)
                    # print("ORIX,OIRY", orix,oriy)
                    
                    # print("CHECK")
                    # print(nx,ny)
                    return False
                q.append((orix,oriy,nx,ny,dist+1))
    return True

def solution(places):
    # room = [[0 for _ in range(5)] for __ in range(5)]
    answer = []
    for r in places:
        q = deque()
        index = 0
        isVisited = [[False for _ in range(5)] for __ in range(5)]
        room = [[p for p in e] for e in r]
        
        for i in range(5):
            for j in range(5):
                if room[i][j] == "P":
                    q.append((i,j,i,j,0))
        
        if bfs(q,isVisited,room):
            answer.append(1)
        else:
            answer.append(0)
    print(answer)
    return answer



solution([["PPPOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]])