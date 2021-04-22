import sys

INF = sys.maxsize

n, m = map(int, list(input().split()))
ANS = -INF
# arr = []

# for i in range(n):
#     arr.append( list(map(int, list(input().split()))))
arr = [[] for _ in range(n)]
for i in range(n):
    temp = list(map(int , input()))

    for e in temp:

        arr[i].append(e)


#print(arr)


for i in range(n):
    for j in range(m):
        for k in range(j+1,m):
            


            if arr[i][j] == arr[i][k]:
                #print(arr[i][k])
                dist = abs(j-k)
                if i + dist < n:
                    if arr[i + dist][j] == arr[i][j] and arr[i + dist][k] == arr[i][j]:
                        temp =(dist + 1) ** 2
                        ANS = max(temp,ANS)
                        
if ANS == -INF:
    print(1)       
else:
    print(ANS)
            

