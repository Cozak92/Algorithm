
import sys
input = sys.stdin.readline

n, m = list(map(int, list(input().split())))

nest = [[1 for _ in range(n)] for __ in range(n)]

# 0의 개수, 1의 개수, 2의 개수

for i in range(m):
    grow = list(map(int, list(input().split())))
    sequence = []

    zeroCnt = grow[0]
    oneCnt = grow[1]
    twoCnt = grow[2]


    for i in range(3):
        for j in range(grow[i]):
            sequence.append(i)

    columSequence = sequence[:n]
    rowSequence = sequence[n-1:]
    #print(columSequence,rowSequence)

    k = 0
    for i in range(n-1,0,-1):
        nest[i][0] += columSequence[k]
        k+=1
    for i in range(n):
        nest[0][i] += rowSequence[i]
    #print(nest)

   
    #print(*nest)
for i in range(1,n):
    print("\n")
    for j in range(1,n):
        nest[i][j] = max(nest[i-1][j-1], nest[i-1][j], nest[i][j-1])
        print(nest[i][j], end=" ")

