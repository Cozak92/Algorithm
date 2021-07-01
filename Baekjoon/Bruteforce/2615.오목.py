board = [list(map(int, input().split())) for _ in range(19)]
dx = [0,0,-1,1,-1,-1,1,1]
dy = [1,-1,0,0,-1,1,-1,1]

for j in range(19): #열 기준으로 탐색
    for i in range(19):

        if board[i][j] != 0:
            
            finder = board[i][j]
            for k in range(8):
                cnt = 1
                nx = i + dx[k]
                ny = j + dy[k]
                px = i - dx[k]
                py = j - dy[k]


                if 0 <= px < 19 and 0 <= py < 19:
                    if board[px][py] == finder: #반대 방향 체크
                        continue

                while 0 <= nx < 19 and 0 <= ny < 19 and board[nx][ny] == finder:
                    #print("nx:" ,nx,"ny:",ny)
                    cnt += 1
                    nx += dx[k]
                    ny += dy[k]
                if cnt == 5:
                    print(finder)
                    print(i+1,j+1)
                    exit()
print(0)