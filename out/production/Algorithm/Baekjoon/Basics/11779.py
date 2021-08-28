import sys
import heapq

input = sys.stdin.readline
INF = sys.maxsize



def djik(start):

    pq = []

    
    costInfo[start] = 0

    heapq.heappush(pq,(costInfo[start],start))

    while pq:

        curCost, curCity = heapq.heappop(pq)

        if curCost > costInfo[curCity]:
            continue

        for nextCity, nextCost in busInfo[curCity]:
            if nextCost + curCost < costInfo[nextCity]:
                costInfo[nextCity] = nextCost + curCost
                trace[nextCity] = curCity
                heapq.heappush(pq,(costInfo[nextCity],nextCity))
                
    
    
    return print(costInfo[endCity])



# def backtraking(endCity):




#        for prevCity, prevCost in busBackInfo[endCity]:

#         if costInfo[prevCity] > costInfo[endCity]:
#             continue
#         if costInfo[endCity] == costInfo[prevCity] + prevCost:
#             route.add(prevCity)
#             backtraking(prevCity)



N = int(input())
M = int(input())


busInfo = [[] for _ in range(N+1)]
busBackInfo = [[] for _ in range(N+1)]
trace = [ 0  for _ in range(N+1)]
costInfo = [INF] * (N+1)


for __ in range(M):
    start, end, cost = map(int, list(input().split()))

    busInfo[start].append((end,cost))
    busBackInfo[end].append((start,cost))


# print(busInfo)
# print(busBackInfo)
startCity, endCity = map(int, list(input().split()))

djik(startCity)

# route = set()

# backtraking(endCity)

# print(len(route))

# for i in route: print(i, end=' ')

path =[endCity]
tracer = trace[endCity]
#print(trace)

while tracer != 0:
    path.append(tracer)
    tracer = trace[tracer]

print(len(path))
print(*path[::-1])



