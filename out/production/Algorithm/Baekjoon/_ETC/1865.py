
def dijkstra(start):
    savedDistance[start] = 0
    q = []

    q.append([start,0])

    while q:
        current, distance = q.pop()

        if savedDistance[current] < distance:
            continue
            
        for i in range(len(roads)):

            if roads[current][i] is not 0:
                NEXT = i
                nextDistance = distance + roads[current][NEXT]

                if(nextDistance < savedDistance[NEXT]):
                    savedDistance[NEXT] = nextDistance
                    q.append(NEXT, nextDistance)

    for j in range(len(wormholes)):
        if wormholes[current][j] is not 0:
            NEXT = j
            nextDistance = distance + wormholes[current][NEXT]

            if(nextDistance < savedDistance[NEXT]):
                savedDistance[NEXT] = nextDistance
                q.append(NEXT, nextDistance)
       
           
    
      


            




T = int(input())
N, M, W = map(int, list(input().split()))


for _ in range(T):
    N += 1
    roads = [[0] *  N for _ in range(N) ]
    wormholes = [[0] *  N for _ in range(N) ]
    savedDistance = [0 for _ in range(N)]

    for i in range(M):
        
        start, end, distance = map(int, list(input().split()))


        roads[start][end] = distance
        roads[end][start] = distance
    
    for j in range(W):

        start, end, distance = map(int, list(input().split()))

        wormholes[start][end] = distance


    print(dijkstra(0))











