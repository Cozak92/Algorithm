n = int(input())
cnt = 0

# y check = check column / no need to check row
# x+y = check right top to right down diagonal
# x-y+n-1 = check left top to left down diagonal
isUsed1 = [False for _ in range(n)]
isUsed2 = [False for _ in range(2*n)]
isUsed3 = [False for _ in range(2*n)]
def func(cur):
    global cnt
    if cur == n:
        cnt += 1
        return
    for i in range(n):
        if isUsed1[i] or isUsed2[cur+i] or isUsed3[cur-i+n-1]:
            continue
        isUsed1[i] = True
        isUsed2[cur+i] = True
        isUsed3[cur-i+n-1] = True
        func(cur+1)
        isUsed1[i] = False
        isUsed2[cur+i] = False
        isUsed3[cur-i+n-1] = False
        
func(0)

print(cnt)