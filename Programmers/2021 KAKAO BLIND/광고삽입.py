# def solution(play_time, adv_time, logs):

#     time = [ ] #0 for _ in range(len(logs))

    
#     for i in range(len(logs)):
#         startTime, endTime = logs[i].split("-")
    
#         hh1, mm1, ss1 = map(int,list(startTime.split(":")))
#         hh2, mm2, ss2 = map(int,list(endTime.split(":")))
#         adStartTime = (hh1*3600) +(mm1*60) + ss1
#         adEndTime = (hh2*3600) + (mm2*60) + ss2

#         time.append([adStartTime,adEndTime])

#     time.sort()
#     saveDict = {} #(start,end) : 0 for start,end in time
    

#     start = 0
#     end = time[0][1]
#     SUM = 0
#     cnt = 1

#     for i in range(len(time)-1):

#         if end > time[i+1][0]:
#             if start == 0:
#                 start = time[i+1][0]
#             cnt += 1

#             print(end,time[i+1][0],cnt)
#             SUM += (end - time[i+1][0]) * cnt
            
#             print(SUM)
#             saveDict[start,end] = (SUM) 
            
#         else:
            
#             end = time[i+1][1]
#             start = 0
#             cnt = 1
#             SUM = 0
            
        
#     print(saveDict)
#     print(time)
        

#     answer = ''
#     return answer

import string
import sys

INF = sys.maxsize


def solution(play_time, adv_time, logs):

    checkedTime = [0] * 360000

    x,y,z = map(int,list(play_time.split(":")))
    play_time = (x*3600) + (y*60) + z
    x,y,z = map(int, list(adv_time.split(":")))
    adv_time = (x*3600) + (y*60) + z

    if play_time <= adv_time:
        return "00:00:00"
 

    times = []

    for time in logs:

        startTime, EndTime = time.split("-")

        hh1, mm1, ss1 = map(int,list(startTime.split(":")))
        hh2, mm2, ss2 = map(int, list(EndTime.split(":")))

        adStartTime = (hh1*3600) + (mm1*60) + ss1
        adEndtime = (hh2*3600) + (mm2*60) + ss2

        checkedTime[adStartTime] += 1
        checkedTime[adEndtime] += -1

    
    for i in range(1,play_time):
        checkedTime[i] += checkedTime[i-1]
    for i in range(1,play_time):
        checkedTime[i] += checkedTime[i-1]


    # resultSum = checkedTime[adv_time]
    # advIndex = 0

    # SUM = 0
    # for start in range(adv_time,play_time):

    #     SUM = checkedTime[start] - checkedTime[start-adv_time]

    #     if SUM > resultSum:
    #         resultSum = SUM
    #         advIndex = start - adv_time+1


    start = adv_time
    res = -INF
    advIndex = 0

    for end in range():
        temp = checkedTime[end] - checkedTime[start] 
        #print(start)

        if temp > res:
            #print(start)
            res = temp
            advIndex = start + 1
        end += 1




   
    tempSum = 0
    resultSum = 0
    start = 0

    sumTimes =[]


    hour ,minutes = divmod(advIndex,3600)
    minutes, sec = divmod(minutes,60)

    hour = str(hour)
    minutes = str(minutes)
    sec = str(sec)

    hour = hour.zfill(2)
    minutes = minutes.zfill(2)
    sec = sec.zfill(2)

    print(hour)


    

    answer = ":".join(([hour,minutes,sec]))


    print(answer)

    return answer

        
    

    #print(checkedTime)



logs = ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]

solution("02:03:55","00:14:15",logs)