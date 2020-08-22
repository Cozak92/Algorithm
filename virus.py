#백준 2606 문제


from collections import deque

def bfs(matrix,visit):
    queue = deque()

    queue.append(1)
    visit[1] = True

    cnt = 0;

    
    
    while queue:
        x = queue.popleft()

        for nx in range(len(matrix[x])):
            if visit[nx] == False and matrix[x][nx]:
                queue.append(nx)
                visit[nx] = True
                cnt += 1


    return cnt


n = int(input())
m = int(input())


matrix = [[0] * (n+1) for _ in range(n+1)]
visit = [False] * (n+1)


for _ in range(m):
    link = list(map(int, input().split()))
    matrix[link[0]][link[1]] = 1 #[1, 2]가 들어오면 1 -> 2, 2 -> 1 양방향 간선 구현
    matrix[link[1]][link[0]] = 1

print(bfs(matrix,visit))


