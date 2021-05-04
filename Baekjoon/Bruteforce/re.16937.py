#https://yabmoons.tistory.com/278

import sys
input = sys.stdin.readline

h, w = map(int, input().split())
n = int(input())
sks = []
for i in range(n):
    sks.append(list(map(int, input().split())))

def check(s1, s2):
    # garo
    if s1[0] + s2[0] <= w and max(s1[1], s2[1]) <= h:
        return True
    # sero
    if s1[1] + s2[1] <= h and max(s1[0], s2[0]) <= w:
        return True
    return False
ans = 0
for i in range(n - 1):
    for j in range(i + 1, n):
        s1 = sks[i]
        s2 = sks[j]
        area = s1[0] * s1[1] + s2[0] * s2[1]
        for k in range(1 << 2):
            s1 = sks[i]
            s2 = sks[j]
            if 1 << 1 & k:
                s1 = list(reversed(sks[i]))
            if 1 << 0 & k:
                s2 = list(reversed(sks[j]))
            if check(s1, s2):
                ans = max(area, ans)
print(ans)