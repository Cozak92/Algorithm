import sys
input = sys.stdin.readline

INF = sys.maxsize

t = int(input())

# def dfs(cur,end,move):
   
#     if cur >= end:
#         return 0
#     #print("cur",cur)
#     #print("move",move)
#     if dp[cur] != INF:
#         return dp[cur]
#     print(move)
#     for i in range(2):
 
#             #print("i",i)
#             #print("cur", cur)
#             #print("jump to", cur+arr[i]+move)
#         dp[cur] = min(dp[cur],dfs(cur+arr[i]+move,end,arr[i]+move) + 1)


#     return dp[cur]

t = int(input())

for _ in range(t):
    x, y = map(int,input().split())
    distance = y - x
    count = 0  # 이동 횟수
    move = 1  # count별 이동 가능한 거리
    move_plus = 0  # 이동한 거리의 합
    while move_plus < distance :
        count += 1
        move_plus += move  # count 수에 해당하는 move를 더함
        if count % 2 == 0 :  # count가 2의 배수일 때, 
            move += 1  
    print(count)