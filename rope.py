#백준 2217

import sys

def ropes(arr):
    sorted_arr = sorted(arr, reverse = True)
    Max = 0
    for i in range(len(sorted_arr)):
        if Max < sorted_arr[i] * (i + 1):
            Max = sorted_arr[i] * (i + 1)

    return Max

N = int(input())
arr = []

for i in range(N):
    print(i)
    arr.append(int(sys.stdin.readline())) 

print(ropes(arr))
