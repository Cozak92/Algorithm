def dfs(x,y):
    visit[x][y] = True
    global cnt
    cnt += 1

    for k in range(4):
        nx, ny = x+dx[k], y+dy[k]
        if 0 <= nx < N and 0 <= ny < N:
            if visit[nx][ny] == False and matrix[nx][ny] == 1:
                visit[nx][ny] = True
                dfs(nx,ny)

    
    return

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

N = int(input())

# list 형태로 input을 받은것을 int로 변환해주고 그것을 List 형태로 n번 받는다
#즉 이차원 배열
matrix = [list(map(int, list(input()))) for _ in range(N)]
queue = [] # bfs 탐색을 위한 큐
visit = [[False]* N for _ in range(N)] # 방문처리를 위한 배열
comp = [] # 단지 수를 체크할 배열

for x in range(len(matrix)):
    for y in range(len(matrix)):
        if visit[x][y] == False and matrix[x][y] == 1:
            cnt = 0;
            dfs(x,y)
            comp.append(cnt)

comp.sort()

print(len(comp), *comp, sep='\n')


