from collections import defaultdict
from collections import deque


import sys

input = sys.stdin.readline



n = int(input())
weight = list(map(int, list(input().split())))
tree = defaultdict(list)
dp = [[0 ,0 ] for __ in range(n+1)]
isVisited = [False] * (n+1) 
answer = deque()

def dfs(current):
    isVisited[current] = True

    dp[current][0] = 0
    dp[current][1] = weight[current-1]


    for adjNode in tree[current]:
        if not isVisited[adjNode]:
          
            dfs(adjNode)
            dp[current][0] += max(dp[adjNode][0], dp[adjNode][1])
            dp[current][1] += dp[adjNode][0]


# def backtracking(current,isIncluded,cnt): #트리는 간선이 2개로 내려갈수도 있어서 쓸 수 없었음

#     cnt += 1

#     if cnt > n:
#         return


 
#     if isIncluded:
#         answer.appendleft(current)
#         for adjNode in tree[current]:
#             #print(dp[adjNode][0])
#             if dp[adjNode][0] + weight[current - 1] == dp[current][1]: #현재노드가 참여한 최고값 - 참여안한 인접노드의  최고값 = 현재 노드의 가중치라면 그 노드가 당첨
#                 backtracking(adjNode,False,cnt)
#     else:
#         #print("chheck")
#         for adjNode in tree[current]:
            
#             if dp[adjNode][0]  == dp[current][0]:
#                 backtracking(adjNode,False,cnt)
#             elif dp[adjNode][1] == dp[current][0]:
#                 backtracking(adjNode,True,cnt)

tracingResult = []
isTraced = [False] * (n+1)

def tracing(current,pre): # 1이라면 이전 값이 포함됨 0이라면 포함되지 않음

    isTraced[current] = True

    if pre: #이전 값이 포함됐으면 현재값은 포함 못함
        for adjNode in tree[current]:
            if not isTraced[adjNode]:
                tracing(adjNode,0)
    else: #이전값이 포함되지 않음
        if dp[current][1] > dp[current][0]: #현재 값을 포함하는 값이 더크다면

            tracingResult.append(current)

            for adjNode in tree[current]:
                if not isTraced[adjNode]:
                    tracing(adjNode,1)
        else:
            for adjNode in tree[current]:
                if not isTraced[adjNode]:
                    tracing(adjNode,0)








    
            


for line in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

dfs(1)   



print(max(dp[1][0],dp[1][1]))
print(dp)

tracing(1,0) # 루트노드의 이전값은 없으므로 0

tracingResult.sort()

print(*tracingResult)


