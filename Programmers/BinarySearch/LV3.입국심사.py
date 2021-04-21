def solution(n, times):
    answer = 0

    #최소시간 , 최대시간
    #최소시간은
    start = (min(times) * n) //len(times)
    end = max(times) * n

    mid = (start+ end) // 2
    while start <= end:
        howMany = 0
        mid = (start+ end) // 2

        for examiner in times:

            howMany += mid // examiner
        
        if howMany < n:
            start = mid + 1
            
        else:
            end = mid - 1
            answer = mid




   
    return answer