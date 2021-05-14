import sys
INF = sys.maxsize

n = int(input())
plask = list(map(int,input().split()))
s = 0
e = n-1
ans = abs(plask[s] + plask[e])
ansA = plask[s]
ansB = plask[e]

while s<e:
    ret = plask[s] + plask[e]
    if abs(ret) < ans:
        ans = abs(ret)
        ansA = plask[s]
        ansB = plask[e]

    if ret < 0:
        s += 1
    else:
        e -= 1

print(ansA,ansB)