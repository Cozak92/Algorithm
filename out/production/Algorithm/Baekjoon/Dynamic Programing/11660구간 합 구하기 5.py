import sys
import copy
from collections import deque

input = sys.stdin.readline



n, m = map(int, list(input().split(" ")))

matrix = []
SUM = [ [0 for _ in range(n+1)] for __ in range(n+1) ]

for i in range(n):
    matrix.append(list(map (int,list(input().split(" ")))))

matrix = [[0] * (n+1)] + [[0, *map(int, input().split())] for _ in range(n)]

print(matrix)
    



for i in range(1,n+1):
    for j in range(1,n+1):
        SUM[i][j] = matrix[i - 1][j - 1]


for x in range(len(SUM)):
    for y in range(len(SUM[x]) - 1):
        SUM[x][y+1] += SUM[x][y]
    
for x in range(len(SUM) - 1):
    for y in range(len(SUM[x])):
        SUM[x+1][y] += SUM[x][y]

for _ in range(m):
    x1,y1,x2,y2 = (map (int,list(input().split(" "))))

    # print("SUM[x2][y2] = ", SUM[x2][y2])
    
    # print("SUM[x1 - 1][y2] = ", SUM[x1 - 1][y2])
    # print("SUM[x2][y1 - 1] = ", SUM[x1][y1-1])
    # print("SUM[x1 - 1][y - 1] = ", SUM[x1-1][y1-1])

    print(SUM[x2][y2] - (SUM[x1 - 1][y2] + SUM[x2][y1 - 1]) + SUM[x1-1][y1-1])

   
    
print(SUM)
        



