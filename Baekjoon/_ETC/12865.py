import sys


N , K = list(map(int, list(sys.stdin.readline().split())))

inv = [[]]
for _ in range(1,N+1):
    inv.append(list(map(int,list(sys.stdin.readline().split()))))


#inv = [ list(map(int,list(sys.stdin.readline().split()))) for _ in range(1,N+1) ]


 


dp = [[ 0 for __ in range(K+1) ] for _ in range(N+1) ]





for x in range(1,N+1):
    for y in range(1,K+1):


        if y >= inv[x][0]:
            dp[x][y] = max(dp[x-1][y], dp[x-1][y-inv[x][0]] + inv[x][1])
        else:
            dp[x][y] = dp[x-1][y]



print(dp[N][K])
