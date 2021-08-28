from itertools import combinations
import sys

INF = sys.maxsize

#다시풀기

def findParent(node,graph,parents):

    
    for child in graph[node]:
        if node not in parents[node]:
            parents[node].append(node)
        parents[node].append(child) 
        findParent(child,graph,parents)


def solution(sales, links):
    answer = 0
    parents = [[] for _ in range(len(sales)+1)]
    
    tree = {i : [] for i in range(1,len(sales)+1)}
    for parent, child in links:

        tree[parent].append(child)


    findParent(1,tree,parents)
 

    VISIT = [False] * (len(sales)+1)
    print(parents)

    for i in range(len(parents)):
        MIN = INF
        if parents[i] != [] and not VISIT[i]:

            for e in range(len(parents[i])):

                MIN = min(MIN,sales[parents[i][e]-1])
                print(parents[i][e],MIN)

            for j in range(i,len(parents)):
                if MIN in parents[j]:
                    VISIT[j] = True
            answer += MIN

        
            

        
    print(answer)
    return answer


sales = [14, 17, 15, 18, 19, 14, 13, 16, 28, 17]
links = [[10, 8], [1, 9], [9, 7], [5, 4], [1, 5], [5, 10], [10, 6], [1, 3], [10, 2]]	
solution(sales,links)