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

    if appl in multitap: 
        pass
    elif 0 in multitap: 
        multitap[multitap.index(0)] = appl
 
    else:
        for app in multitap:
            if app not in appliance[num:]: 
                swap = app
                break
            elif appliance[num:].index(app) > max_I: 
                max_I = appliance[num:].index(app)
                swap = app
        multitap[multitap.index(swap)] = appl
        max_I = swap = 0
        res += 1
    num += 1


print(res)


        





