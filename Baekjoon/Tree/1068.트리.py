
answer = 0
def dfs(cur):
    global answer

    visited[cur] = True

    isLeaf = True
    for adjNode in tree[cur]:
       
        if not visited[adjNode]:
            isLeaf = False
            dfs(adjNode)


    if isLeaf:
        answer += 1

n = int(input())
parent = list(map(int, list(input().split())))

rootNode = 0

tree = [[] for _ in range(n)] 
visited =[False] * n

for i in range(n):
    if parent[i] == -1:
        rootNode = i
        continue

   
    tree[i].append(parent[i])
    tree[parent[i]].append(i)

delNode = int(input())
visited[delNode] = True
if delNode == rootNode:
    print(0)
  
else:
    dfs(rootNode)
    print(answer)