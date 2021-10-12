import sys
sys.setrecursionlimit(10**9)

#dp[현재단어 인덱스][밞아야할단어 인덱스][다리]

scroll = input()
angel = input()
deamon = input()



dp = [[[-1 for _ in range(2)] for __ in range(20)] for ___ in range(100)]    




def finding(cur,find,which):

    if find == len(scroll):
        return 1

    
    if dp[cur][find][which] != -1:
        return dp[cur][find][which]

    res = 0
    
 
    if which == 0:
        for i in range(cur,len(angel)):
           
            if scroll[find] == angel[i]:
                res += finding(i + 1, find + 1, 1)
    
    else:
        
        for j in range(cur,len(deamon)):
            if scroll[find] == deamon[j]:
                res += finding(j + 1, find + 1, 0)    
        
    dp[cur][find][which] = res
    #print(res)
   
    return dp[cur][find][which]


# 1 = deamon
# 0 = angel
print(finding(0,0,1)+finding(0,0,0))
