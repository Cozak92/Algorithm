import sys

def solution(n):

    answer = ''

    if n<=3:
        return '124'[n-1]
    else:
        q, r = divmod(n-1,3)
        # 0(1,2,4)이 없으므로 -1을 해서 처리
        return solution(q-1) + '124'[r]
    return answer


print(solution(43))