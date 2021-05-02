# 출력: 불이 도달하기 전 탈출 불가 - IMPOSSIBLE
    # 미로를 탈출하는 경우 - 가장 빠른 탈출시간

# 지훈, 불을 각각 BFS하여 나갈수 있는 시간 및 여부를 구한다.

from collections import deque

R, C = map(int, input().split())
field = [list(input()) for i in range(R)]
J = None
F = []

for i in range(R):
    for j in range(C):
        if field[i][j] == 'J': J = (i, j)
        if field[i][j] == 'F': F.append((i, j))

q = deque([J])
time = 0
q_fire = deque(F)
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

found = False
while q:
    time += 1

    for i in range(len(q_fire)):
        y, x = q_fire.popleft()

        for j in range(4):
            ny = y + dy[j]
            nx = x + dx[j]

            if 0 <= ny < R and 0 <= nx < C and field[ny][nx] != '#' \
            and field[ny][nx] != 'F':
                field[ny][nx] = 'F'
                q_fire.append((ny, nx))

    for i in range(len(q)):
        y, x = q.popleft()

        for j in range(4):
            ny = y + dy[j]
            nx = x + dx[j]

            if 0 <= ny < R and 0 <= nx < C:
                if field[ny][nx] == '.':
                    field[ny][nx] = 'J'
                    q.append((ny, nx))
            else:
                found = True
                break
        if found: break
    if found: break

    if len(q) == 0:
        time = 'IMPOSSIBLE'
        break

print(time)