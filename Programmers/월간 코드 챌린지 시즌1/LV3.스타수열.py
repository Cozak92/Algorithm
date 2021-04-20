from itertools import combinations
from collections import Counter
import sys

INF = sys.maxsize

from itertools import combinations
from collections import Counter
import sys

INF = sys.maxsize

def solution(a):
    answer = 0

    if len(a) == 1:
        return answer
    

    MAX = -INF
    
    c = Counter(a)

    print(c)

    # 가장 많으 공통부분은 가진것을 기준으로 한다.
    for k, v in c.items():

        if c[k] * 2 < answer:
            continue

        idx = 0
        max_value = k
        length = 0

        while idx < len(a) - 1:
            # idx, idx+1 != max_value의 뜻은 공통부분이 없다.
            # 또 같은값 체크
            if (a[idx] != max_value and a[idx+1] != max_value) or a[idx] == a[idx+1]:
                idx += 1
                continue
            length += 2
            idx += 2
        answer = max(answer, length)


    
    


    # # 수열 a의 부분수열이고 갯수가 짝수개
    # for i in range(2,len(a)+1,2):
    #     #print(i)
    #     check = set()
    #     for item in combinations(a,i):
    #         #print(item)
    #         # 부분수열을 2개씩 짤랐을때 겹치는 부분이 1개이상
    #         flag = True
    #         check.add(item[0])
    #         check.add(item[1])
    #         for j in range(0,len(item),2):
    #             #print(item[j],item[j+1])
    #             if item[j] == item[j+1]:
    #                 flag = False
    #                 break
    #             if not item[j] in check and not item[j+1] in check:
    #                 flag = False
    #                 break
    #             check.add(item[j])
    #             check.add(item[j+1])
            
    #         if flag:
    #             MAX = max(MAX,len(item))


            # for x in item:
            #     check.add(x)
            # if len(check) == (len(item)//2 + 1):
            #     MAX = max(MAX,len(item))

    return answer

solution([0,3,3,0,7,0,2,0])