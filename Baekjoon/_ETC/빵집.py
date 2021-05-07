def solution(bakery_schedule, current_time, k):

    N = len(bakery_schedule)

    bakery_time = [0] * N
    breads = [0] * N
    cnt = 0;

    for i in range(N):
        bakery_time[i] = bakery_schedule[i].split(' ')[0]
        breads[i] = bakery_schedule[i].split(' ')[1]
    # print(bakery_time)
    # print(breads)
    current_time = current_time.split(':')
    print(current_time)

    for i in range(N):
        hours_minutes = bakery_time[i].split(':')
        print(hours_minutes)
        if (hours_minutes[0] >= current_time[0] and hours_minutes[0] >= current_time[0]):
            cnt += int(breads[i])
            print(cnt)
            if( cnt >= k):
                hours = (int(hours_minutes[0]) - int(current_time[0])) * 60
                minutes = int(hours_minutes[1]) - int(current_time[1])  
                return hours + minutes

    return -1


bakery_schedule = ["09:05 10", "12:20 100","13:25 6","14:24 5"]

current_time = "12:05"

k = 10

print(solution(bakery_schedule,current_time,k))