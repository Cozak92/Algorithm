# !!아이디어!! 사각형을 만든다. 안에 삼각형을 채운다. 그냥 삼각형으로 만들어도 되지않나?

def solution(n):
    
    answer = [[0] * x for x in range(1,n+1)]

    x, y = -1, 0
    num = 1
    for i in range(n):
        for j in range(i,n):
            # 모듈러연산으로 어디 부분의 변인지 체크하는게 가장 중요함
            if i % 3 == 0:
                x += 1
            elif i % 3 == 1:
                y += 1
            else:
                x -= 1
                y -= 1
            
            answer[x][y] = num
            num += 1
        
    result = []

    for a in answer:
        result += a    
    
    
    return result
                