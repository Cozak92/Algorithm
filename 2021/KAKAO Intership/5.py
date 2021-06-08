from collections import defaultdict
def solution(k, num, links):
    answer = 0
    SUM = sum(num)
    graph = defaultdict(list)
    for i in range(len(num)):
        graph[i].append(links[i][0])
        graph[i].append(links[i][1])
    
    print(graph)

    return answer