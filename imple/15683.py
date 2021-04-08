

N, M = int(input())

room = [[ x for x in int(input().split())] for _ in range(N) ]


for i in range(N):
    for j in range(M):

        if room[i][j] != 0 and room[i][j] != 6:

            while
