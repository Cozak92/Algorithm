# bfs는 큐로 만들고

def bfs(start):
    visit = [start]
    queue = [start]
    while queue:
        current_node = queue.pop(0)
        for search_node in range(len(matrix[current_node])):
            if matrix[current_node][search_node] and search_node not in visit:
                visit += [search_node]
                queue += [search_node]
    
    return visit

#dfs는 재귀함수

def dfs(current_node, row, visit):
    visit += [current_node]
    for search_node in range(len(row[current_node])):
        if row[current_node][search_node] and search_node not in visit:
            visit = dfs(search_node, row , visit)
    return visit

n, m = map(int, input().split())


matrix = [[0] * (m) for _ in range(n)]



a = [list(map(int, list(input()))) for _ in range(n)]

print(matrix)

print(matrix)