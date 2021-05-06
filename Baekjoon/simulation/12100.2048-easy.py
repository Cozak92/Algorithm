import copy
n = int(input())

board = [list(map(int, input().split())) for _ in range(n)]


def doRotate():
    
    temp = copy.deepcopy(board2)

    for i in range(n):
        for j in range(n):
            board2[i][j] = temp[n - 1 - j][i]
    

def tilt(dir):
    while dir:
        doRotate()
        dir -= 1
    
    for i in range(n):
        index = 0
        tiltted = [0 for _ in range(n)]
        for j in range(n):
            if board2[i][j] == 0: continue #  if board has no number
            if tiltted[index] == 0: tiltted[index] = board2[i][j] # 옮기는 배열에 숫자가 없다면
            elif tiltted[index] == board2[i][j]: 
                tiltted[index] *= 2 # 옮기려는 배열에 숫자가 같다면
                index += 1
            else: #  옮기려는 배열에 숫자가 다르다면
                index += 1
                tiltted[index] = board2[i][j]
            
        board2[i] = tiltted 
ans = 0

for l in range(1<<(2*5)):
    breute = l
    board2 = copy.deepcopy(board)
    for i in range(5):
        dir = breute % 4
        breute = breute // 4

        tilt(dir)

    for num in board2:
        ans = max(ans,max(num))
   
print(ans)


        