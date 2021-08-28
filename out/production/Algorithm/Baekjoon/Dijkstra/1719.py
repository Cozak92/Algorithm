import heapq
import sys
from collections import deque


def checkRoutes(where,end,distFee,cities):
    visit = [False] * (n+1)
    count = 0

    q = deque()

    q.append(end)

    while q:
       
        end = q.popleft()
        temp = distFee[end]


        for checking in where[end]:
            if distFee[checking] > distFee[end] : continue

           


            if distFee[checking] + cities[checking][end] == temp:
                #print('distFee["{0}"] + cities["{0}"]["{1}"] == "{2}"'.format(checking,end,temp))
                #print(distFee[checking], cities[checking][end], temp)
                #print("checking : ", checking)
                #print("end : ", end)
                if (checking,end) not in checkList:
                    checkList.append((checking,end))
                
                    q.append(checking)
    print(checkList)
    for e, v in checkList:
        if e == start:
            count += 1

    return count




def dijkstra(start,end,cities):
    timeFee = [INF] * (n+1)
    q = []

    timeFee[start] = 0
    heapq.heappush(q, (timeFee[start],start))


    while q:

        currentDistFee, currentCity = heapq.heappop(q)

        if timeFee[currentCity] < currentDistFee:
            continue

        for nextCity in cities[currentCity]: 

            nextDistFee = currentDistFee + cities[currentCity][nextCity]

            if nextDistFee < timeFee[nextCity]:

                timeFee[nextCity] = nextDistFee
                heapq.heappush(q, (nextDistFee, nextCity))

    return timeFee
    


input = sys.stdin.readline

INF = sys.maxsize


n, m, start, end = list(map(int, list(input().split())))

checkList = list()


citiesTime = [{} for _ in range(n+1)]
citiesFee = [{} for _ in range(n+1)]



where = [[] for _ in range(n+1)]
#whereFees = [[] for _ in range(n+1)]


for __ in range(m):
    p, r, c, t = list(map(int, list(input().split())))

    citiesTime[p][r] = t
    citiesTime[r][p] = t

    where[r].append(p)
    where[p].append(r)

    citiesFee[p][r] = c
    citiesFee[r][p] = c

    #whereFees[r].append(p)
    #whereFees[p].append(r)


time = dijkstra(start,end,citiesTime)
fee = dijkstra(start,end,citiesFee)

#print(time, fee)

#print("time Check")
timeN = checkRoutes(where,end,time,citiesTime)
#print("fee Check")
feeN = checkRoutes(where,end,fee,citiesFee)

#print(timeN, feeN)

print(timeN * feeN)














