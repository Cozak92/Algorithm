import sys
from collections import deque
INF = sys.maxsize
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
MOD = 1000000007
dy = [1, 0, -1, 0]
dx = [0, -1, 0, 1]
dy8 = [1, 1, 0, -1, -1, -1, 0, 1]
dx8 = [0, -1, -1, -1, 0, 1, 1, 1]

def li(): return list(map(int,input().split()))

n = int(input())

arr = deque(x for x in range(1,n+1))
while len(arr) != 1:
    n = len(arr)
    for i in range(1,n+1):
         x = arr.popleft()
         if i % 2 == 0:
             arr.append(x)

print(arr[0])