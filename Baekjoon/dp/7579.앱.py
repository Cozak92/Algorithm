import sys

input = sys.stdin.readline


n, m = list(map(int, list(input().split())))
memories = list(map(int, list(input().split())))
cost = list(map(int, list(input().split())))

maxCost = sum(cost)


dp = [[-1 for _ in range(maxCost+1)] for __ in range(n+1)]

print(dp)
print(maxCost)


def dping(number,memory):
    print(number,memory)

    if number == 0 or memory < 0:
        return sys.maxsize
    
    if dp[number][memory] != -1:
        
        return dp[number][memory]


    dp[number][memory] = min(dping(number-1,memory- cost[number-1] ) + memories[number-1], dping(number-1,memory))
    print(dp[number][memory])

    return dp[number][memory]

print(dping(n,maxCost))