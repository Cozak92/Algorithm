import sys
input = sys.stdin.readline
t = int(input())

def dfs(cur):
    global cnt
    nex = studnet[cur]

    if not visited[nex]:
        visited[nex] = True
        dfs(nex)
    else:
        if not finished[nex]:
            x = nex
            cnt += 1
            while cur != x:
                x = studnet[x]
                cnt += 1
            
    finished[cur] = True
for i in range(t):


    n = int(input())
    cnt = 0
    studnet = [0] + list(map(int,list(input().split())))
    visited = [False for _ in range(n+1)]
    finished = [False for _ in range(n+1)]

    for i in range(1,n+1):
        if not visited[i]:
            visited[i] = True
            dfs(i)

    print(n-cnt)