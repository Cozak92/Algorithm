import sys
INF = sys.maxsize
n = int(input())
arr = [0] * (n+1)

def tracking(index,open1,open2):
    if index == m:
        return 0

    if dp[index][open1][open2] != -1:
        return dp[index][open1][open2]
    
   
    
    open1Cnt = tracking(index + 1, order[index], open2) + abs(order[index] - open1)
    open2Cnt = tracking(index + 1, open1, order[index]) + abs(order[index] - open2)

    dp[index][open1][open2] = min(open1Cnt,open2Cnt)

    return dp[index][open1][open2]





a, b = map(int,list(input().split()))
order = []


m = int(input())
for i in range(m):
    order.append(int(input()))

dp = [[[-1 for _ in range(n+1)] for __ in range(n+1)] for ___ in range(m)]



tracking(0,a,b)

print(dp[0][a][b])



            

        
    
    
