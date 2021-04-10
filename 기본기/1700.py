# 첫 알고리즘은 각 전자제품 숫자를 세고 꼽혀있는것 중 가장 적은것을 뺏지만
# 그 방법으로는 최적화를 할 수 없었따

import sys

input = sys.stdin.readline
INF = sys.maxsize

N, K = map(int,list(input().split()))
appliance = [ int(x) for x in input().split()]

multitap = [0] * N
res = swap = num = max_I = 0

for appl in appliance:

    if appl in multitap: #해당 전자제품이 멀티탭에 꽂혀있음
        pass
    elif 0 in multitap: #만약 멀티탭에 빈 공간이 남아있다면 꽂아줌
        multitap[multitap.index(0)] = appl
 
    else:
        for app in multitap:
            if app not in appliance[num:]: #만약 꽂혀있는 전자제품이 이후에 안쓰면 바로 뽑아버린다
                swap = app
                break
            elif appliance[num:].index(app) > max_I: # 리스트에 잇다면 꽂혀있는 전자제품 중에 쓰이는 가장 나중에 것을 뽑아버린다.
                max_I = appliance[num:].index(app)
                swap = app
        multitap[multitap.index(swap)] = appl
        max_I = swap = 0
        res += 1
    num += 1


print(res)


        





