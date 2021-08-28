import sys
INF = sys.maxsize
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
MOD = 1000000007
dy = [1, 0, -1, 0]
dx = [0, -1, 0, 1]
dy8 = [1, 1, 0, -1, -1, -1, 0, 1]
dx8 = [0, -1, -1, -1, 0, 1, 1, 1]

def li(): return list(map(int,input().split()))


n, k = li()

cnt = 0
for h in range(n):
    for m in range(60):
        for s in range(60):
            temp = ""
            if h < 10 : temp += "0"
            temp += str(h)
            if m < 10 : temp += "0"
            temp += str(m)
            if s < 10 : temp += "0"
            temp += str(s)
            if k in temp: cnt += 1
print(cnt)
