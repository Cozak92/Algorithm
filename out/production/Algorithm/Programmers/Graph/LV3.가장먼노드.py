# import heapq
# import sys

# INF = sys.maxsize

# def djik(start,matirx,dist):

#     pq = []
#     dist[start] = 0
    

    

#     heapq.heappush(pq,[dist[start],start])

#     while pq:

#         curDist, curNode = heapq.heappop(pq)

#         if curDist > dist[curNode]:
#             continue

#         for nextNode in range(1,len(matirx[curNode])):
#             nextDist = matirx[curNode][nextNode]
#             if curDist + nextDist < dist[nextNode]:
#                 dist[nextNode] = curDist + nextDist
#                 heapq.heappush(pq,[dist[nextNode],nextNode])

    
#     print(dist)
    
#     return dist
    

# def solution(n, edge):

#     dist = [INF] * (n+1)
#     answer = 0
#     matirx = [[ INF  for _ in range(n+1)] for __ in range(n+1)]

#     for start,end in edge:

#         matirx[start][end] = 1
#         matirx[end][start] = 1

#     dist = djik(1,matirx,dist)



#     cnt = 0
#     MAX = -INF

#     for i in dist:
#         if i != INF:
#             if MAX == i:
#                 answer +=1
#             MAX = max(MAX,i)
            
            

#     return answer

import sys
from collections import deque
from collections import defaultdict

INF = sys.maxsize


def bfs(start,matirx,dist):

    visit = [False] * (len(matirx) +1)
    dist[start] = 0
    visit[start] = True
    q = deque()
    q.append(start)

    while q:

        cur = q.popleft()

        for nex in matirx[cur]:
            if not visit[nex]:
                print(nex)
                dist[nex] = dist[cur] + 1
                visit[nex] = True
                q.append(nex)

    return dist




def solution(n, edge):

    dist = [-1] * (n+1)
    answer = 0
    matirx = defaultdict(lambda: [])

    for start,end in edge:

        matirx[start].append(end)
        matirx[end].append(start)

    print(matirx)

    dist = bfs(1,matirx,dist)



    answer = dist.count(max(dist))

    print(answer)

    return answer





solution(6,[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]])