import sys
sys.setrecursionlimit(10**9)
n, s = list(map(int,input().split()))
arr = list(map(int, input().split()))
answer = 0

def func(index,k):
    global answer
    if index == n:
        if k == s:
            answer += 1 
        return
    func(index+1,k)
    func(index+1,k+arr[index])

func(0,0)
if s == 0: answer -= 1
print(answer)

