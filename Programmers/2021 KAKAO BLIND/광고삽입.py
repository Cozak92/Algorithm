def solution(play_time, adv_time, logs):

    time = [ ] #0 for _ in range(len(logs))

    
    for i in range(len(logs)):
        startTime, endTime = logs[i].split("-")
    
        hh1, mm1, ss1 = map(int,list(startTime.split(":")))
        hh2, mm2, ss2 = map(int,list(endTime.split(":")))
        adStartTime = (hh1*3600) +(mm1*60) + ss1
        adEndTime = (hh2*3600) + (mm2*60) + ss2

        time.append([adStartTime,adEndTime])

    time.sort()
    saveDict = {} #(start,end) : 0 for start,end in time
    

    start = 0
    end = time[0][1]
    SUM = 0
    cnt = 1

    for i in range(len(time)-1):

        if end > time[i+1][0]:
            if start == 0:
                start = time[i+1][0]
            cnt += 1

            print(end,time[i+1][0],cnt)
            SUM += (end - time[i+1][0]) * cnt
            
            print(SUM)
            saveDict[start,end] = (SUM) 
            
        else:
            
            end = time[i+1][1]
            start = 0
            cnt = 1
            SUM = 0
            
        
    print(saveDict)
    print(time)
        

    answer = ''
    return answer


logs = ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]

solution('a','a',logs)