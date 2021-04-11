import sys

N , M = list(map(int, list(sys.stdin.readline().split())))
S = [list(map(int, list(sys.stdin.readline().split()))) for _ in range(M)]

q = []

for i in range(M):

    if S[i][1] not in q:
        q.append(S[i][1])
    else:
        if S[i][0] in q:
            q.remove(S[i][0])
            
        
    q.insert(0,S[i][0])

    

for x in range(1,N+1):
    if x not in q:
        q.append(x)

print(q)