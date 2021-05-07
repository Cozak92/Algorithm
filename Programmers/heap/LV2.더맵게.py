import heapq

def solution(scoville, K):
    answer = 0
    pq = []
    for i in range(len(scoville)):
        heapq.heappush(pq,scoville[i])


    while len(pq) != 1:
        answer += 1

        
        lowest = heapq.heappop(pq)
        sLowest = heapq.heappop(pq)

        newFood = lowest + ( sLowest * 2)
        heapq.heappush(pq, newFood)

        if pq[0] > K:
            return answer
    

    return -1


print(solution([1, 2, 3, 9, 10, 12], 7))
