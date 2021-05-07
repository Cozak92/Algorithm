from collections import deque

n = int(input())
dp = [0] * (n+1)
isVisited = [False] * (n+1)
dx = [3,2,1]

q = deque()
q.append(1)

while q:

    x = q.popleft()

    for operate in dx:

        if operate == 1:
            nx = x + 1
        else:
            nx = x * operate

        if nx <= n:
            if not isVisited[nx] or dp[nx] > dp[x] + 1:
                isVisited[nx] = True
                dp[nx] = dp[x] + 1
                q.append(nx)

print(dp[n])


