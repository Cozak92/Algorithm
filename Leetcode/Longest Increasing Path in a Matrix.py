def bfs(x,y,matrix):
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    visit = [False for _ in range(len(matrix))]

    queue = []
    trackArr = []
    queue.append(x,y)
    trackArr.append([x,y])

    while queue:
        curX, curY = queue.pop(0)

        for i in range(4):
            nx, ny = curX + dx[i], curY + dy[i]

            if 0 <= nx < len(matrix) and 0 <= ny < len(matrix):
                if matrix[nx][ny] - matrix[curX][curY] > 0:
                    trackArr.append([nx,ny])
                    queue.append(nx,ny)
                else:
                    trackArr.remove([curX,curY])
    
    return len(trackArr)






