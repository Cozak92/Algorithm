

def bfs(n,computers,visit):
    queue=[]
    net = 0

    for i in range(n):
        if visit[i] == False:
            net += 1
            visit[i] = True
            
            start = i
            print("시작 :", start)
            queue.append(start)

            while(queue):

                x = queue.pop()
                print("x :", x)

                for j in range(0,n):
                    if computers[x][j] and visit[j] == False:
                        queue.append(j)
                        visit[j] = True

            

    return net

            



def solution(n, computers):

    visit = [False] * n

    print(visit)


    return bfs(n,computers,visit)



print(solution(	3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))






    