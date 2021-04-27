n, w, l = list(map(int, list(input().split())))

trucks = list(map(int, list(input().split())))

queue = []
cnt = 0

for i in range(n):
    while True:
        if len(queue) == w:
            queue.pop(0)
        if sum(queue) + trucks[i] <= l:
            break
        else:
            queue.append(0)
            cnt += 1
            
    queue.append(trucks[i])
    cnt +=1
        



print(cnt+w)