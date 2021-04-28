import sys
from collections import defaultdict
input = sys.stdin.readline


def bfs():

    q = []

    for i in range(1,n+1):
        if indegree[i] == 0:
            dp[i] = buildTime[i]
            q.append([i,buildTime[i]])
 
    #print(q)
   
    while q:

        curNode, curTime = q.pop(0)
        #visited[curNode] = True

        for nextNode in graph[curNode]:


            nextTime = buildTime[nextNode]
            
            
            if nextTime + curTime > dp[nextNode]:
                dp[nextNode] = nextTime + curTime
                
            indegree[nextNode] -= 1

            if indegree[nextNode] == 0:
                q.append([nextNode,dp[nextNode]])






t = int(input())


for ___ in range(t):
    n, k = list(map(int, list(input().split())))
   

    buildTime = [0] + list(map(int, list(input().split())))

    #print(buildTime)

    dp = [0 for _ in range(n+1)] 
    indegree = [0 for _ in range(n+1)]

    graph = defaultdict(list)

    for i in range(k):
        
        x, y = list(map(int, list(input().split())))

        graph[x].append(y)
        indegree[y] += 1

    #print(indegree)

    w = int(input())

    bfs()


    print(dp[w])
