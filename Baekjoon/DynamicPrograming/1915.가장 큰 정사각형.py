import sys
import copy
input = sys.stdin.readline
n, m = list(map(int, input().split()))
board = [[] for _ in range(n)]
for i in range(n):
    temp = input().rstrip()
    for t in temp:
        board[i].append(int(t))

board2 = copy.deepcopy(board)
if n == 1 or m == 1:
    print(1)
    exit()
ans = 0
for i in range(1,n):
    for j in range(1,m):
        if board[i][j]:
            board2[i][j] = min(board2[i-1][j], board2[i][j-1], board2[i-1][j-1]) + 1
            ans = max(ans,board2[i][j])
print(ans*ans)
