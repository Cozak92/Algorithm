def solution(progresses, speeds):
    answer = []
    cnt = 0

    while progresses:
    
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        
        if progresses[0] >= 100:
            #print(progresses)
            cnt = 1
            for i in range(1,len(progresses)):
                if progresses[i] >= 100:
                    cnt += 1
                else:
                    break
            for i in range(cnt):
                progresses.pop(0)
                speeds.pop(0)
            answer.append(cnt)
                
            

            
    
    return answer