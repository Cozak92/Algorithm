def solution(answers):
    n = len(answers)
    firCnt, secCnt, thiCnt = 0, 0 ,0
    fir = [1, 2, 3, 4, 5]
    sec = [2, 1, 2, 3, 2, 4, 2, 5]
    thi = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    for i in range(n):
        if answers[i] == fir[i%5]:
            firCnt += 1
        if answers[i] == sec[i%8]:
            secCnt += 1
        if answers[i] == thi[i%10]:
            thiCnt += 1
    MAX = max(firCnt,secCnt,thiCnt)     
    tempAnswer = [firCnt,secCnt,thiCnt]
    answer = []
    
    for i in range(1,4):
        if MAX == tempAnswer[i-1]:
            answer.append(i)
    return answer

s = "017"
sN = int(s)

print(sN)