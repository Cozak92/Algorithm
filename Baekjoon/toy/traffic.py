def checktr(time,li):
    start = time
    end = start + 1000
    temp = 0

    for i in li:
        if start <= i[1] and i[0] < end:
            temp += 1

    return temp



def solution(lines):

    # split으로 나누고 시간은 초단위로 계산
    li= []
    answer = 0


    for line in lines:
        i,t,s = line.split()
        t = t.split(":")
        s = float(s.replace('s','')) * 1000
        end =(int(t[0]) * 3600 + int(t[1]) * 60 + float(t[2])) * 1000

        start = (end - s) + 1
        li.append([start,end])


    for l in li:

        answer = max(answer,checktr(l[0],li),checktr(l[1],li))

        





    return answer



lines = ["2016-09-15 01:00:10.000 10.0s", "2016-09-15 01:00:04.000 0.5s"]
print(solution(lines))