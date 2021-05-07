import sys
import heapq


# graph = [ [distance], [distance].... ]

# grpah[0][0]

def dijkstra(N,start,graph):

    visit = [False] * N

    dist = [sys.maxsize()] * N

    dist[start] = 0

    pq = []

    heapq.heappush(pq, [0,start])

    while pq:
        minValue, index = heapq.heappop(pq)
        visit[index] = True

        for edge in graph[start]:



