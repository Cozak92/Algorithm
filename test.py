from collections import defaultdict

def solution(s,e,skips):

    DICT = defaultdict(str)
    SUM = 0
    q = ""

    for _ in range(len(skips)):
        SUM += skips[_]
        DICT[SUM] += e[_%len(e)]

    
    print(DICT)

    curIndex = 0
    for x in DICT:
        print(len(s))
        if x > len(s):
            break

        for i in range(curIndex,x):
            print(i)
            
            if DICT[x][0] == s[i]:
                print(DICT[x])
                print("check")
                q += DICT[x][0]
                DICT[x] = DICT[x].replace(s[i],"")
                print(DICT[x][0])
            q += (s[i])
        curIndex = x
        q += DICT[x]
    

    if x < len(s):
        q += s[x:]


    print(q)





s = "I love coding"
e = "maskos"
skips = [0,0,3,2,7,0]

solution(s,e,skips)