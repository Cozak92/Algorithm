s = input()
mult = {'(': 2, ')': 2, '[': 3, ']': 3}
pair = {'(': ')', '[': ']', ')': '(', ']': '['}
stack = []
ans, cur = 0, 1

# 브라켓 문제를 풀땐 스택을 이용하자.
for c in s:
    if c in '([':
        stack.append(c)
        cur *= mult[c] #왜 곱할까? 왜냐면 곱한 cur값만큼 브라켓 겹쳐 있다는 뜻이다.
    elif c in ')]':
        if not stack or stack[-1] != pair[c]:
            ans = 0
            break
        if prev == pair[c]:
            ans += cur # 따라서 브라켓이 하나 끝날때마다 문제 지시대로 현재 겹쳐있는 값을 더해준다.
        stack.pop()
        cur //= mult[c] #왜 나눌까? 왜냐면 해당 브라켓이 끝났으므로 해당 브라켓 값만큼 나눠주어서 더 이상 곱하기 연산이 안들어가게 한다.
    prev = c

if stack:
    ans = 0

print(ans)


