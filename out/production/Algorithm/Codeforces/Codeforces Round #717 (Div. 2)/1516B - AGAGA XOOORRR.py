#https://codeforces.com/contest/1516/problem/B

# 나중에 유투브로 강의 보기

import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):

    n = int(input())

    arr = list(map(int ,list(input().split())))

    xr = 0

    for e in arr:
        xr ^= e
    
    if not xr: # xr == 0 이라는 뜻은 모든 수가 같다.
        print("YES")

    else: # 같지않다면 확인
        temp , counter = 0, 0
        for e in arr:
            temp ^= e
            if temp == xr:
                counter += 1
                temp =0
        if counter >= 3:
            print("YES")
        else:
            print("NO")


 

