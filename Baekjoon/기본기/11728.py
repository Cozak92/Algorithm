import sys
input = sys.stdin.readline

N, M = map(int,list(input().split()))

A = list(input().split())
B = list(input().split())
C = set()
C = (A+B)
C.sort()

for i in C: print(i, end='')

