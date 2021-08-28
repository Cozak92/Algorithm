import sys

INF = sys.maxsize

def floyd(n,graph):

    for mid in range(1,n+1):
        for start in range(1,n+1):
            for end in range(1,n+1):

                if graph[start][end] > graph[start][mid] + graph[mid][end]:
                    graph[start][end] = graph[start][mid] + graph[mid][end]

# def dfs(commonFare,start):




#     graph[start][i] + graph[i][endOfA] + dfs()





#     return 



def solution(n, s, a, b, fares):
    nodes = n
    start = s
    endOfA = a
    endOfB =b 
    
    graph = [[INF for _ in range(nodes+1)] for __ in range(nodes+1)]
    
    answer = INF
    
    
    for i in range(1,nodes+1):
        for j in range(1,nodes+1):
            if i == j:
                graph[i][j] = 0
                
    for info in fares:
        city1, city2, cost = info
        
        graph[city1][city2] = cost
        graph[city2][city1] = cost
            
    floyd(nodes,graph)



    # answer = graph[start][endOfA] + graph[start][endOfB]

    for i in range(1,nodes+1):
        answer = min(answer,graph[start][i] + graph[i][endOfA] + graph[i][endOfB])

    print(answer)
    return answer



solution(6,4,6,2,[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]])