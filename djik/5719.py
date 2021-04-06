import sys
import heapq

input = sys.stdin.readline
INF = sys.maxsize
def dijkstra(start,end,graph):

    distance = [INF] * (N+1)

    pq = []

    distance[start] = 0

    heapq.heappush(pq,(distance[start],start))

    while pq:

        currentDist, currentNode = heapq.heappop(pq)

        if distance[currentNode] < currentDist: continue

        for nextNode in graph[currentNode]:

            nextDist = currentDist + graph[currentNode][nextNode]

            if nextDist < distance[nextNode]:
                distance[nextNode] = nextDist
                heapq.heappush(pq,(nextDist,nextNode))
             
        if currentNode == end:
            break
    
    return distance

def backtraking(graph,end):
    temp = distance[end]
    #print(temp)

    for i in where[end]: # 현재 정점으로 모이는 전 노드들
        if distance[i] > distance[end]: # 전 노드까지의 최소값이 현재의 최소값보다 크다면 볼 필요도 없다.
            continue

        elif distance[i] + graph[i][end] == temp: # 현재 정점에 모이는 전 노드들의 엣지 + 전 노드들까지의 최소값 = 현재 노드까지의 최소값이라면 최단거리다.
            if (i,end) not in delete: # 체크 안할시 시간초과
                delete.add((i,end))
                backtraking(graph,i)








while True:
    N, M = list(map(int, list(input().split())))

    if N + M == 0:
        quit()


    graph = [{} for _ in range(N+1)]
    where = [[] for _ in range(N+1)]
    S, D = list(map(int,list(input().split())))

    for _ in range(M):
        U, V, P = list(map(int,list(input().split())))

        graph[U][V] = P
        where[V].append(U) # 한 정점에 모이는 다른 정점을 보기위해 만듬.

    delete = set()

    distance = dijkstra(S,D,graph)
    backtraking(graph,D)

    for a,b in delete:
        del graph[a][b]

    temp = dijkstra(S,D,graph)[D]

    if temp == INF :
        print(-1)
    else:
        print(temp)



        







