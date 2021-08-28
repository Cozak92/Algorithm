#가장 많은 독립집합을 찾는 문제
# 많은 독립집합을 N의 갯수에서 빼주면 얼리어답터의 갯수가된다.

import sys
from collections import defaultdict
from collections import deque
sys.setrecursionlimit(10**6)


input = sys.stdin.readline
INF = sys.maxsize


def dfs(current):
    isVisited[current] = True
    dp[current][0] = 0
    dp[current][1] = 1

    for adjNode in tree[current]:
        if not isVisited[adjNode]: # 방문하지 않았다는 이야기는 자식노드라는 뜻
            dfs(adjNode)
            dp[current][1] += dp[adjNode][0] #현재를 포함하면 자식은 포함안함
            dp[current][0] += max(dp[adjNode][1],dp[adjNode][0])



n = int(input())
isVisited = [False] * (n+1)


dp = [[0,0] for _ in range(n+1)]
#dp[i][1] = 참여했을때
#dp[i][0] = 참여안했을때

tree = defaultdict(list)

for i in range(n-1):
    x, y= list(map(int, list(input().split())))

    tree[x].append(y)
    tree[y].append(x)

dfs(1)
print(n - max(dp[1][0],dp[1][1]))





# for i in range(1,n+1):
#     injected = [False] * (n+1)
#     early = [False] * (n+1) 
#     q.append(i)
#     earlyCnt = 0
#     while q:

#         current = q.popleft()
#         #print("current = ", current )

#         for adjNode in tree[current]:

#             if not injected[adjNode] and not early[adjNode]:
                
#                 if not early[current]:
#                     #print("CHECK")
#                     early[current] = True
#                     earlyCnt += 1
#                     #print(earlyCnt)
#                 injected[adjNode] = True

#                 q.append(adjNode)


   





    



