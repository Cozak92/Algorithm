
import sys
input = sys.stdin.readline

n, m = list(map(int, list(input().split())))

nest = [[1 for _ in range(n)] for __ in range(n)]

# 0의 개수, 1의 개수, 2의 개수

for i in range(m):
    grow = list(map(int, list(input().split())))
  

    zeroCnt = grow[0]
    oneCnt = grow[1]
    twoCnt = grow[2]

    for i in range(zeroCnt,zeroCnt+oneCnt):
        nest[i]


   
    #print(*nest)
for i in range(1,n):
    print("\n")
    for j in range(1,n):
        nest[i][j] = max(nest[i-1][j-1], nest[i-1][j], nest[i][j-1])
        print(nest[i][j], end=" ")

