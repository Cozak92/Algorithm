import sys

#dfs?? bfs??
INF = sys.maxsize
dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(robot,board,cnt):
    x1, y1, x2, y2 = robot

    if x1 == len(board) -1 and y1 == len(board) -1 and x2 == len(board)-1 and y2 == len(board)-1:
        return cnt
    
    
    flag = False
    
    for i in range(4):
        
        nx1, ny1 = x1 + dx[i], y1 + dy[i]
        nx2, ny2 = x2 + dx[i], y2 + dy[i]
        
        if 0 <= nx1 < len(board) and 0 <= ny1 < len(board) and 0 <= nx2 < len(board) and 0 <= ny2 < len(board):
            if board[nx1][ny1] != 1 and board[nx2][ny2] != 1:
                flag = True
                nextRobot = [nx1,ny1,nx2,ny2]
                cnt = min(cnt,bfs(nextRobot,board,cnt + 1))

    if not flag:
        return INF
    #왼쪽 위 두개를 빼서 상태를 알아보자
    
        

def solution(board):

    robot = [0,0,0,1]
    cnt = 0
    
    answer = 0
    return answer