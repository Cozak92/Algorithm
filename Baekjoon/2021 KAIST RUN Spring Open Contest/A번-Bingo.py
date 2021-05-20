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

n,k = li()
s = n -2
q = [ 0 for _ in range(n)]
for i in range(n):
    if i == 0:
        q[i] = i
    elif i == n - 1:
        q[i] = i
    else:
        q[i] = s
        s -= 1

if n == 2:
    if k > 1: 
        print("NO")
        quit()

if k <= n*n -n:
        print("YES")
        cnt = 0

        for i in range(n):
            for j in range(n):
                if j == q[i]:
                    print("." , end = "")
                    continue
                if cnt < k :
                    print("#", end="")
                    cnt += 1
                else: print(".", end= "")
            print()
        
else: print("NO")
    

