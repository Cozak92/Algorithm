def solution(n):
    answer = []
    while n > 0 :
        
        t = n % 3
        n = n //3
        
        answer.append(t)
    
    #sorted(answer, reverse = True)
    #print(answer)
    ans = 0
    j = len(answer)
    for i in range(len(answer)):
        j -= 1
        ans += (3**i) * answer[j]
        
        
    
    

    
    return ans