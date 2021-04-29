# https://www.youtube.com/watch?v=G-9-_2f5NKQ&t=189s&ab_channel=%EB%A1%9C%EB%B0%8D%EB%A7%A8
import copy
import itertools

def solution(n, weak, dist):
    
    copyedDist = copy.deepcopy(dist)
    copyedDist.sort(reverse = True)
    #
    for i in range(1,len(dist)+1): #1명이 들어갈때 두명이 들어갈때 .. 몇명이 들어가야하나?

        for item in itertools.combinations(range(len(weak)), i): # 친구 숫자 만큼 뽑아 // 직접 아이템을 가져오면 인덱스 계산하기 어려우므로 몇번 인덱스를 가져오는지로 체크
            picked = []

            for j in range(i): #거리 구하기
                picked.append((weak[item[( j + 1) % i] - 1] - weak[item[j]] + n) % n)
                # 거리를 구하는 코드가 상당히 긴데 하나씩 설명해 보도록 하겠다

                # weak[item[( j + 1) % i] - 1] - weak[item[j]] 이 부분은 취약포인트가 현재 지점과 다른 여러지점으로 나뉘는데 
                # 그 중에서 우리가 거리를 구해야 할 곳은 선택된 지점중 현재 지점의 다음 지점의 직전까지이다.
                # 그 부분을 표현 하기위해 item[( j + 1)] - 1로 표현 한것이고 혹시나 j+1이 item의 길이를 넘을 때 우리는 다음 지점이 필요한것이 아니라 원형이므로 
                # i로 나누어서 모듈러 연산으로 표현한것이다. 그 이후 현재 아이템의 값을 뺀다.


                #  이후 n으로 나눠준것은 역시나 원형임을 고려해서 현재 아이템이 10이고 1 까지의 거리를 구할때 그냥 빼버리면 -9가 나오지만 n만큼을 더하면 3이라는 정상적인 숫자가 나온다.
                # 그리고 나머지 결과값이 음수가 아닌 양수의 경우 그냥 n을 더하고 놔두면 거리의 값이 n의 값을 넘어가므로 다시 n만큼 모듈러 연산을 통해 해결해준다.

            picked.sort(reverse = True) # 큰 값부터 비교하는 이유는 친구또한 큰 값 부터 비교했으므로 

            flag = True

            for j in range(i): #각각의 값을 비교해서 하나라도 거리가 크면 순찰을 못도는것이므로 실패
                if picked[j] > copyedDist[j]:
                    flag = False
                    break
            if flag:   
                return i #만약 전부다 체크가 되면 현재 들어간 친구들이 총 숫자!

    
    
    answer = -1
    return answer