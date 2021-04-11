

#백준 1932
import sys

def solution(N):
    # arrTest = [[7],
    #             [3,8],
    #             [8,1,0],
    #             [2,7,4,4],
    #             [4,5,2,6,5]]
    ex_line = list(map(int, sys.stdin.readline().split(" ")))

    for i in range(1,N):
        # arr.append(list(map(int, input().split()))) # 입력방식 기억해두자
        arr = list(map(int, sys.stdin.readline().split(" ")))
        arr[0] += ex_line[0] # arr을 바로 받고 전 라인에 0번을 더해준다 // 어차피 0번은 맨왼쪽이므로 0번 밖에 더할게 없으므로
        arr[i] += ex_line[i-1] # 맨오른쪽은 반대로 i-1값을 더해준다
        for j in range(1,i):
            arr[j] += max(ex_line[j], ex_line[j-1])
        ex_line = arr
           

    return max(arr)


print(solution(int(input())))