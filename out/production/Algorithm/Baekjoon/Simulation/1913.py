

N = int(input())
checkedNumber = int(input())
checkedIndex = []
cen = (N-1) // 2

def makeMatrix(i,j):
    lev = max(abs(i),abs(j))
    value = (lev * 2 + 1) ** 2
    
    diff = lev * 2

    if j == -lev: return value -(lev+i)
    value -= diff
    if i == lev: return value -(lev+j)
    value -= diff
    if j == lev: return value - (lev-i)
    value -= diff
    return value - (lev-j)


matrix = [[ 0 for _ in range(N)] for _ in range(N)]

for i in range(-cen,cen+1):
    for j in range(-cen,cen+1):
        matrix[i+cen][j+cen] = makeMatrix(i,j)


for x in range(N):
    for y in matrix[x]:
        if y == checkedNumber:
            checkedIndex = (x,matrix[x].index(y))
        print(y, end=' ')
    print("\n", end='')

# for x in makeMatrix:
#     print(" ".join(map(str, x))

for _ in checkedIndex:
    print(_+1, end=" ")
  