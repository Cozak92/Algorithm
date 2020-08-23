# 백준 2173번
# bfs하면 자동으로 최단거리가 나옴
#왜 최단거리르 따로 구하려고하니 병신아

def bfs():
    queue = []
    queue.append([0,0]) # 좌표를 큐에 담아 BFS 탐색
    visit[0][0] = True # 방문했는지 체크
    dist [0][0] = 1 #거리 체크용

    while len(queue) != 0:
        x, y= queue.pop(0) #큐에 있는 맨 첫번째 요소르 뺌
        for k in range(4):
            nx, ny = x+dx[k], y+dy[k] # 좌표 값 게산
            if 0 <= nx < n and 0 <= ny < m: # 인덱스 범위를 넘어서면 안되므로 예외처리 
                if visit[nx][ny] == False and matrix[nx][ny] == matrix[x][y]: #만약 방문 한적없고 해당 좌표값이 1이라면 이동할수 있다.
                    queue.append((nx,ny)) # 방문할 수있는 좌표값을 넣어준다
                    dist[nx][ny] = dist[x][y] + 1 # 그리고 해당 거리까지 가는 거리는 현재 까지 거리의 +1
                    visit[nx][ny] = True # 해당좌표를 방문 처리해준다.

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


