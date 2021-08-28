#https://www.acmicpc.net/problem/10282

import heapq
import sys

input = sys.stdin.readline

INF = sys.maxsize


def dijkstra(start,graph):
    q = []
    global seconds 
    seconds = [INF] * (N+1)        
    seconds[start] = 0

    heapq.heappush(q, (seconds[start],start))
       #print(start)
        #print(visit)

    while q:

            #print(q)

        sec, current = heapq.heappop(q)
        if seconds[current] < sec: #방문체크 부분
            continue

        for nextNode in graph[current]:
            totalDist = sec + graph[current][nextNode]


            if totalDist < seconds[nextNode]:
                seconds[nextNode] = totalDist
                heapq.heappush(q, (totalDist,nextNode))

    count = 0
    totalInfectedTime = -1

    for second in seconds:

        if second != INF:
            
            #print(second)
            totalInfectedTime = max(totalInfectedTime,second)
            count += 1

    #print(N,d,c)
    print(count,totalInfectedTime)


T = int(input())

for __ in range(T):

    N, d, c = list(map(int, list(input().split())))
    #print(N,d,c)
 
    graph = [{} for _ in range(N+1)]

    for m in range(d):
        a,b,s = list(map(int, list(input().split())))
        graph[b][a] = s

    dijkstra(c,graph) 
  
            

        

