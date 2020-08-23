from collections import deque

def solution(drum):

    N = len(drum)
    print("drum size :", N)

    queue = deque()
    startQ = deque()


    cnt = 0

    start =[0,0]
    startQ.append(start)





    while startQ:

        check = 0


        start = startQ.popleft()

        queue.append(start)

        print("cnt :", cnt)
        print("new start")

        while queue:


            x, y= queue.popleft()
            print(y,x)

            if x >= N :
                return cnt

            if y >= N:
                cnt += 1
                startQ.append([start[0]+1 , start[1]])
                break


            if (drum[y][x] == '#'):
                print("#")
                nx, ny = x,y+1
                queue.append((nx,ny))
            elif(drum[y][x] == '>'):
                print(">")
                nx, ny = x+1, y
                queue.append((nx,ny))
            elif(drum[y][x] == '<'):
                print("<")
                nx, ny = x-1,y
                queue.append((nx,ny))
            elif(drum[y][x] == '*'):
                check += 1
                nx, ny = x,y+1
                queue.append((nx,ny))
                print("check :", check)
                if check >= 2:
                    queue.clear()
                    startQ.append([start[0]+1 , start[1]])
                    break




    return -1

 


# drum = ["######",
# "******",
# ">>>>*<",
# "#<#>>#",
# ">#*#*<",
# "######"]


drum = ["#####",
">>**<",
"#####",
"#*#*#",
"#*#*#"]


print(solution(drum))