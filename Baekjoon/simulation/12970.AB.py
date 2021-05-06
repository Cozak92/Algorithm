n, k = list(map(int, list(input().split())))

half = n // 2
s = []
for i in range(half):
    s.append( "A")
for i in range(half,n):
    s.append("B")

MAX = half * (n-half) # 해당 배열에서 얻을수 있는 최대쌍

front = half - 1 # A의 문자열들중 가장 마지막 문자
back = n - 1 # B의 문자열들중 가장 마지막 문자

if k > MAX: 
    print(-1)
    exit()

target = MAX - k 

# n = 5, k = 4인 경우를 생각해보면 앞에서 s배열은 "AABBB"가 될것이고
# 따라서 n = 5로 최대로 만들수 있는 쌍의 갯수는 6개다.
# 여기서 현재 최대 만들수있는 갯수에서 k개를 빼면 줄여야되는 쌍의 갯수가 나온다.
# 6 - 4 = 2이므로 우리가 줄여야 되는 쌍의 갯수는 2개이다.
# 따라서 A들중 가장 마지막에 위치한 A를 뒤로 2만큼 움직여주면 해당 쌍의 갯수만큼 줄일 수 있다.


while target > 0:
    if target >= n-half:  # n-half 보다 크다면 한 쌍을 0개로 만들 수있음
        s[front], s[back] = s[back], s[front] #A 문자열을 끝으로 보내면 쌍이 0개가 된다.
        front -= 1
        back -= 1
        target -= n - half
    else: # n-half 보다 작다면 맞는 수만큼 뒤로 움직여서 숫자조정
        s[front], s[front+target] = s[front+target], s[front]
        target = 0

print("".join(s))