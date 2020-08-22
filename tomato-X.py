#백준 7576

import sys
from collections import deque #그냥 배열보다 큐로 쓰는게 더 빠르다
r = sys.stdin.readline


def bfs(M, N, box):
    # 좌우상하
    dx = [0, 0, 1, -1]
    dy = [-1, 1, 0, 0]

    days = -1

    while ripe:
        days += 1
        for _ in range(len(ripe)): #이미 배열에 들어가있느 익은 토마토들 수만큼 진행해줌 // 왜냐하면 동시에 진행해야 하니까
            x, y = ripe.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if (0 <= nx < N) and (0 <= ny < M) and (box[nx][ny] == 0):
                    box[nx][ny] = box[x][y] + 1 # visit boolean 해당 배열이 익은걸로만 체크
                    ripe.append([nx, ny])

    for b in box: #큐가 비었는데 박스앞에 0이 남아있다면 접근하지 못한거니까 -1 // 
        if 0 in b:
            return -1
    return days


M, N = map(int, r().split())
box, ripe = [], deque()
for i in range(N):
    row = list(map(int, r().split()))
    for j in range(M):
        if row[j] == 1: #1인 모든 토마토를 큐에 먼저 넣음. 동시에 시작하는거랑 같음
            ripe.append([i, j])
    box.append(row) #박스에 row값을 넣어줌


print(bfs(M, N, box))