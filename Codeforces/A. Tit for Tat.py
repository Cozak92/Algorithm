import sys
from itertools import combinations

input = sys.stdin.readline


t = int(input())

for _ in range(t):

    n, m = map(int, list(input().split(" ")))
    arr = list(map(int, list(input().split(" "))))

