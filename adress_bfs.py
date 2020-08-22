#dx[0] dx[0] = 위쪽
#dx[1] dx[1] = 왼쪽
#dx[2] dx[2] = 아래
#dx[3] dx[3] =오른쪽

#백준 2667번
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

N = int(input())

# list 형태로 input을 받은것을 int로 변환해주고 그것을 List 형태로 n번 받는다
#즉 이차원 배열
matrix = [list(map(int, list(input()))) for _ in range(N)]
queue = [] # bfs 탐색을 위한 큐
visit = [[False]* N for _ in range(N)] # 방문처리를 위한 배열
comp = [] # 단지 수를 체크할 배열




# 시작점을 먼저 찾아야함

for i in range(len(matrix)):
    for j in range(len(matrix)):
        cnt = 0;
        if visit[i][j] == False and matrix[i][j] == 1:
            start = i, j
            visit[i][j] = True
            queue.append(start)
            cnt += 1;

            while len(queue) != 0:
                x, y = queue.pop(0)
                for k in range(4):
                    nx, ny = x+dx[k], y+dy[k]
                    if 0 <= nx < N and 0 <= ny < N:
                        if visit[nx][ny] == False and matrix[nx][ny] == 1:
                            visit[nx][ny] = True
                            queue.append((nx,ny))
                            cnt += 1;

            comp.append(cnt)

comp.sort()

print(len(comp), *comp, sep='\n')
