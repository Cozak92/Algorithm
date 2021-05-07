#twopointer
import sys

input = sys.stdin.readline

INF = sys.maxsize

N, S = map(int, list(input().split()))

seq = [int(x) for x in input().split()]


cnt = seq[0]
start, end = 0, 1
MIN = INF
SUM = [0] * (N + 1)

for i in range(1,N+1):
    SUM[i] = SUM[i-1] + seq[i-1]
    
#print(SUM)

while start < N:

    # print("합 ", cnt)
    cnt = SUM[end]-SUM[start]
    #print(cnt)

    if cnt < S:
        # print("end 늘어남")
        # print("start, end = ", start,end)
        
        if end != N:
            end += 1
        else:
            start += 1
    elif cnt >= S:
        # print("start 늘어남")
        # print("start, end = ", start,end)

        MIN = min(MIN, end - start)
        start += 1
        # print("MIN = ", MIN)

    

if MIN == INF:
    print(0)
else:
    print(MIN)


    

     


            
        