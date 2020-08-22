# 백준 2173번
# bfs하면 자동으로 최단거리가 나옴
#왜 최단거리르 따로 구하려고하니 병신아

def bfs():
    queue = []
    queue.append([0,0])
    visit[0][0] = True
    dist [0][0] = 1

    while len(queue) != 0:
        x, y= queue.pop(0)
        for k in range(4):
            nx, ny = x+dx[k], y+dy[k]
            if 0 <= nx < n and 0 <= ny < m:
                if visit[nx][ny] == False and matrix[nx][ny] == 1:
                    queue.append((nx,ny))
                    dist[nx][ny] = dist[x][y] + 1
                    visit[nx][ny] = True

    return dist[n-1][m-1]

# dx[0], dy[0] => 오른쪽
# dx[1], dy[1] => 왼쪽
# dx[2], dy[2] => 아래
# dx[3], dy[3] => 위
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

n, m = map(int, input().split())

matrix = [list(map(int, list(input()))) for _ in range(n)] #배열 입력

visit = [[False]*m for _ in range(n)]

dist = [[0] * m for _ in range(n)] #거리 체크용



print(bfs())


