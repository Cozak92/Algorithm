import sys

input = sys.stdin.readline

d, n, m = list(map(int,input().split()))


stones = [0] +[int(input()) for _ in range(n)] + [d]

dp = [-1 for _ in range(n+2)]

print(sorted(stones))
ans = mid
start = 0

end = d


# 이분탐색

while start <= end:
    mid = (start+end) // 2

    # pos == 현재 돌섬의 위치
    # cnt == 스킵해야되는 갯수
    pos, cnt = 0, 0


    for i in range(1,len(stones)):

        if stones[i] - stones[pos] < mid: # 만약 뛰는 거리가 현재 뛰어야하는거리 보다 작다면

            cnt += 1 # 스킵해야되는 갯수 +1

        else:

            pos = i # 크다면 현재 돌섬의 위치는 i

    if cnt > m: # 스킵해야되는 갯수가 정해진것보다 많다면

        end = mid - 1 #뛰어야 되는 거리를 줄여보자

    else:
        start = mid + 1 # 뛰어야 되는거리 늘려보기
        ans = mid

print(ans)



