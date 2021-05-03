import sys
from collections import defaultdict
INF = sys.maxsize



def leastBricks(wall):

    ##########################################################
    # answer = INF

    # row = sum(wall[0])
    # column = len(wall)
    # #0 for _ in range(row)

    # bricks = [[] for __ in range(column)]
    # #print(bricks)

    # for i in range(column): # row는 필요 없었다
    #     for m in range(len(wall[i])): #wall 안에 몇개 들어있는지에 따라
    #         for k in range(wall[i][m]): # wall 안에 숫자만큼 반복
    #             bricks[i].append(m)

    # #print(bricks)



    # for x in range(row-1):
    #     brickCnt = 0
    #     if bricks[0][x] == bricks[0][x+1]:
    #         brickCnt += 1
    #     for y in range(1,column):
    #         if bricks[y][x] == bricks[y][x+1]:
    #             brickCnt += 1
    #     print(x,brickCnt)
    #     answer = min(answer,brickCnt)

    # return (answer if answer != INF else len(wall))

    ########################시간초과##########################

    

    ############아이디어##########
    # 각 로우를 더 해가면서 체크한다.
    # 더한 값이 존재한다면 틈이 있다는 뜻이다. (길이가 같으니까)
    # 해쉬맵에 해당 값이 몇번 등장하는지 저장한다.
    # 가장 많이 등장하는 값에서 컬럼의 길이를 빼면 막혀잇는 블록의 갯수다.

    empty = defaultdict(int)
    column = len(wall)
    answer = 0

    for row in wall:
        rows = 0
        for brick in row:
            rows += brick
            print(brick,rows)
            if rows != sum(wall[0]): # 가장 마지막 값은 확인 하지 않는다.
                empty[rows] += 1
                answer = max(answer,empty[rows])
    print(empty)
    
    return column - answer






wall = [[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]

leastBricks(wall)