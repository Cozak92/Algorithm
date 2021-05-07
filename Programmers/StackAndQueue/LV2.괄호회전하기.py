from collections import deque
Braket = {"(": ")", "{": "}", "[":"]"}


def isCorrect(braket):
    stack = []

    for b in braket:
        if b in Braket:
            stack.append(b)
        else:
            if(stack):
                t = stack.pop()
                if b != Braket[t]:
                    return False

            else:
                return False
    if stack:
        return False
    return True


def solution(s):
    answer = 0
    n = len(s)
    s = deque(s)

    for i in range(n):
        if isCorrect(s):
            answer += 1
        t = s.popleft()
        s.append(t)

    return answer


print(solution("{{{{{{{"))
