from queue import PriorityQueue

def solution(food_times, k):
    if sum(food_times) <= k:
        return -1
    
    answer = 0
    q = PriorityQueue()
    
    for i in range(len(food_times)):
        q.put((food_times[i],i+1))
    
    sum_time = 0
    pre = 0
    now_len = len(food_times)
    
    # 시간을 더해서 그 시간이 K보다 커지면 남은 배열 확인
    while sum_time + ((q.queue[0][0] - pre) * now_len) <= k: 
        now = q.get()[0]
        sum_time += (now - pre) * now_len
        now_len -= 1
        pre = now
    
    remainder_time = k - sum_time  # 남은 시간은 k - 현재까지 더한시간
    food_len = len(q.queue) # 현재 남은 음식수
    res = sorted(q.queue, key = lambda x : x[1]) #인덱스 순으로 정렬
    print(res)
    temp = remainder_time//food_len 
    # 남은 초 // 남은 음식 = 남은 음식을 한번씩 더 먹을 수 있는 횟수
    remainder_time -= temp * food_len
    # 더 먹을 수 있는 시간을 타깃 시간에서 빼줌.
    
    
    return res[remainder_time][1]

    



#f = [ 946, 314, 757, 322, 559, 647, 983, 482, 145 ]
f = [8, 6, 4]
#k = 1833
k = 15
print(solution(f,k))