import sys
answer = -sys.maxsize

n, m = list(map(int,input().split()))
s = [list(map(int,input().split())) for _ in range(n)]

#print(s)
for i in range(m):
    for j in range(i+1,m):
        for k in range(j+1,m):
            sums = 0
            for a in range(n):
                sums += max(s[a][i], s[a][j],  s[a][k])
            answer = max(sums,answer)

print(answer)