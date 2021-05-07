import sys
import heapq

input = sys.stdin.readline
INF = sys.maxsize



def djik(start,end):
    pq = []

    costInfo = [INF] * (citiesNum+1)
    #print(costInfo)
    costInfo[start] = 0
    heapq.heappush(pq,(costInfo[start],start))


    while pq:

        curCost, curCity = heapq.heappop(pq)

        if costInfo[curCity] < curCost:
            continue

        for nextCity, nextCityCost in busInfo[curCity]:
            #print(nextCity)
            if curCost + nextCityCost < costInfo[nextCity]:
                costInfo[nextCity] = curCost + nextCityCost
                heapq.heappush(pq,(costInfo[nextCity],nextCity))
        
    
    #print(costInfo)
    return print(costInfo[endCity])

citiesNum = int(input())
busNum = int(input())

#print(costInfo)

busInfo = [[] for i in range(citiesNum+1)] #원래는 딕셔너리 자료형을 사용했는데 같은 노선이 있다는 것을 체크 안해서 1시간 날림

for i in range(busNum):
    start, end, cost = map(int, list(input().split()))
    busInfo[start].append((end,cost))

#print(busInfo)

startCity, endCity = map(int, list(input().split()))

djik(startCity,endCity)





