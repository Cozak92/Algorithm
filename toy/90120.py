import sys

N = int(sys.stdin.readline())


for i in range(N):
    cnt = 0
    S = list(sys.stdin.readline().rstrip())
    for k in S:
        if k == "(" :
            cnt += 1
        elif k == ")":
            cnt -= 1

        if cnt < 0:
            print("NO")
            break


    
    if not cnt:
        print("YES")
    else:
        print("NO")
    