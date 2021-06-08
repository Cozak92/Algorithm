from collections import defaultdict
import heapq
import sys

INF = sys.maxsize

def djik(n,start,traps,graph,distance,isOpen,end):
    
    pq = []
    distance[start] = 0
    
    heapq.heappush(pq,(distance[start],start))
    
    while pq:
        currentDist, currentNode = heapq.heappop(pq)
        if currentNode == end:
            break
        #print(currentDist,currentNode)
        #if currentDist > distance[currentNode]:
            #continue
        for nextNode in graph[currentNode]:
            for nextDist in graph[currentNode][nextNode]:

                # print("CUR,NEXT" , currentNode,nextNode)
                if currentNode in traps:

                    if isOpen[currentNode][nextNode]: #열려 있는 상태라면 이제 닫힘
                        # print("Closed")

                        isOpen[currentNode][nextNode] = False
                        isOpen[nextNode][currentNode] = True
                    
                       
                    else: # 닫혀있는 상태라면 이제 열림
                        # print("OPEN")
                        for i in range(n+1):
                            isOpen[currentNode][nextNode] = True
                            isOpen[nextNode][currentNode] = False
                        totdist = nextDist + currentDist
                        #if distance[nextNode] > totdist:
                        distance[nextNode] = totdist
                        heapq.heappush(pq,(distance[nextNode],nextNode))

                        
                else:
                    if isOpen[currentNode][nextNode]: # 입력할때 트랩 상관없이 앞뒤로 다 넣었으므로 체크
                        totDist = nextDist + currentDist
                        #if distance[nextNode] > totDist:
                        distance[nextNode] = totDist
                        heapq.heappush(pq,(distance[nextNode],nextNode))
        #print(pq)

         
           
                
            


def solution(n, start, end, roads, traps):
    distance = [INF] * (n+1)
    isOpen =[[False for _ in range(n+1)] for _ in range(n+1)]
    graph = [{ x : [] for x in range(n+1)} for _ in range(n+1)]
    for x,y,dist in roads:
        graph[x][y].append(dist)
        isOpen[x][y] = True
        graph[y][x].append(dist)
    
    # print(graph)
    djik(n,start,traps,graph,distance,isOpen,end)
    # print(distance[end])
    # print(distance)
    # print(distance)
    return distance[end]


solution(	4, 1, 4, [[1, 2, 1], [3, 2, 1], [2, 4, 1]], [2, 3])