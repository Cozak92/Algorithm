def solution(s):
    cnt =[0,0] #[1] = 제거된 0의 갯수, [0] = 작업 갯수
    answer = []

    while 1:

        cnt[0] += 1

        while "0" in s:
            cnt[1] += 1
            s = s.replace("0","",1) # 그냥하면 바로 다 바꿔버림 카운트를 할 수가 없다.
            

        s = format(len(s),'b')
        #print(s)
        #s = int(str(len(s)), 2)

        s = str(s)

        if s == "1":
            break

    return cnt

solution("01110")