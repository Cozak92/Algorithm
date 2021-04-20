def solution(a):
    answer = 1 #최소값은 무조건 되니까 일단 1
    MIN = min(a)

    for i in range(2):
        
        curMin = a[0]
        i = 1

        while curMin != MIN: #가장 최소값을 만나기 전까지 돈다
            if curMin > a[i]: #현재 최소값이 새로만난 값보다 크다면
                curMin = a[i] # 새로만남 값이 새로운 정답이 될 수 있다.
                answer += 1
            i += 1
        a.reverse()

            

    
    return answer