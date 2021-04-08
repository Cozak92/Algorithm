

a, b=  map(int,list(input().split()))

n, m = map(int,list(input().split()))


# b 값만 반대로 체크
MAP = [[ 0 for _ in range(a)] for __ in range(b)]
direction = {'N': (-1, 0), 'E': (0, 1), 'S': (1, 0), 'W':(0, -1)}

heading = ["N","E","S","W"]

robot = [[0] for _ in range(n+1)] 
#print(robot)

for i in range(1,n+1):
    posA, posB, head = list(input().split())
    posB, posA = int(posB),int(posA)

    robot[i] = [head,b-posB,posA-1]
    MAP[b - posB][posA-1] = i


for j in range(m):
    robotNum, order, orderNum  = list(input().split())
    robotNum, orderNum = int(robotNum),int(orderNum)
    print(robot[robotNum])
    nb, na = robot[robotNum][1], robot[robotNum][2]
    ob, oa = robot[robotNum][1], robot[robotNum][2]

    
    if order == "F":
        db, da = direction[robot[robotNum][0]]

        for __ in range(orderNum):

            nb +=  db
            
            na +=  da

            print(nb,na)
            
            print(db,da)

            

            if 0 <= na < a and 0 <= nb < b:
                if MAP[nb][na]:
                    print('Robot {} crashes into robot {}'.format(robotNum, MAP[nb][na]))
                    quit()


            else:
                print('Robot {} crashes into the wall'.format(robotNum))
                quit()

        if 0 <= na < a and 0 <= nb < b:       
            MAP[ob][oa] = 0
            MAP[nb][na] = robotNum
            robot[robotNum][1], robot[robotNum][2] = nb,na
    
    else:
        findingHeading = heading.index(robot[robotNum][0])
        #print(findingHeading)
        #print(robot[robotNum][0])
        for ___ in range(orderNum):
            
            # print(heading.index(robot[robotNum][0]))
            # print(robot[robotNum][0])

            if order == "L":
                findingHeading -= 1
            else:
                findingHeading += 1


        robot[robotNum][0] = heading[findingHeading%4]
        #print(robot[robotNum][0])
    # if ans:
    #     print(ans)
    #     break
    

print("OK")
                

            


