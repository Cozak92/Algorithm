def solution(s):
    leng = []
    res = ""
   

    if len(s) == 1:
        return 1
    
    for i in range(1,len(s)//2+1):
        c = 1
        r = s[:i]
        
        for j in range(i,len(s),i):
            if s[i:j+i] == r:
                c += 1
            else:
                if c == 1:
                    c =""
                res += str(c) + r
                r = s[i:j+i]
                c = 1

        if c == 1:
            c = ""
        res += str(c) + r
        leng.append(len(res))
        res = ""
        
    return min(leng)


print(solution("aabbaccc"))


