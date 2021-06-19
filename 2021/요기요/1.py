# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
from collections import defaultdict

def solution(S, C):
    dicts = defaultdict(int)
    names = []
    realName = ""
    ans = ""


    name = ""
    i = 0

    for i in range(len(S)):
        if name == "" and S[i] == " ":
            continue
        
        if S[i] == "," or i == len(S) - 1:
            if i == len(S) - 1:
                name += S[i]
            temp = name.split(" ")
            if(len(temp) > 2): #미들네임 처리
                names.append(temp[0] + " " + temp[2])
            else: names.append(temp[0] + " " + temp[1])
            
            
            temp2 = names[-1].lower().replace("-","")
            temp2 = temp2.split(" ")
            temp2 = ".".join(temp2) #이메일용 이름
            if dicts[names[-1]] != 0:
                ans += name+" <"+temp2+str(dicts[names[-1]]+1)+"@"+C.lower()+".com>, "
            else: ans += name+" <"+temp2+"@"+C.lower()+".com>, "
            dicts[names[-1]] += 1
            name = "" 
            continue
        name += S[i]
        
    

    ans = ans[0:-2]

    return(ans)
    
