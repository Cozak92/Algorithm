


import sys
from collections import deque

#백준 1463번

dx = [3,2,1]

def solution():

    queue = deque()
    queue.append(1)
    visit = [False] * (number+1)


    while queue:
        
        x = queue.popleft()

        for i in range(len(dx)):

            if i == 2:
                nx = x + 1
            else:
                nx = x * dx[i]

            if nx <= number:
                if visit[nx] == False or (dp[x] + 1 < dp[nx]):
                
                    visit[nx] = True
                    queue.append(nx)
                    dp[nx] = dp[x] + 1  
        
    
    return






number = int(input())

dp = [0] * (number+1)

solution()

print(dp[number])

