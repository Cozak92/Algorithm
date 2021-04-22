import sys

INF = sys.maxsize

# # 성냥개비별 필요 갯수를 적어 놓는다 딕셔너리로
# # 해당 성냥개비 N개로 무엇을 만들 수 있는지 다 만들어 본다.
# #  dfs? 
# # 그중 가장 작은수와 가장 큰수를 저장한다.



# T = int(input())
# MAX = -INF
# MIN = INF   

# def dfs(w,n,info,num):
#     # 0으로 시작할수 없음
#     if num == "" and w == "0":
#         return
#     n -=  info[w]
#     # w를 만드는데 드는 성냥개비를 뺀다.
#     if n < 0: # 부족하다면 없음
#         return
#     num += w
#     num = int(num)
    
#     if dp[n][0] < num and dp[n][1] > num:
#         return
#     #print(num)
#     #print(dp[n][0])

#     dp[n][0] = min(dp[n][0],num)
#     dp[n][1] = max(dp[n][1],num)

# for _ in range(T):

    

#     info = {"1":2, "2":5, "3":5, "4":4, "5":5, "6":6, "7":3, "8":7, "9":6, "0":6}
#     check = []

#     n = int(input())
#     dp = [[INF,-INF] for _ in range(n+1) ]

#     for i in range(10):
#         dfs(str(i),n,info,"")

  

#     print(dp[0][0],dp[0][1])


    



#     for i in range(10):

#         dfs(str(i),n,info,str(num)) 
        
            
def getMax(num):
    ret = ""

    if(num%2): 
        ret += "7"
        num -= 3
    
    t = num // 2

    ret += "1" * t

    

    return ret

def getMin(num):
    add = ["1", "7", "4", "2", "0", "8"];
    # 2개일때 최소 값.. 3개일때 최소 값...

    MIN = [INF] * 101
    MIN[2] = 1;
    MIN[3] = 7;
    MIN[4] = 4;
    MIN[5] = 2;
    MIN[6] = 6; 
    MIN[7] = 8;
    MIN[8] = 10

    for i in range(9,num+1):
        for j in range(2,8):
            curr = str(MIN[i - j]) + add[j-2];
            print(curr)
            MIN[i] = min(MIN[i], int(curr))

    return MIN[n]


    

T = int(input())


for _ in range(T):

    

    info = {"1":2, "2":5, "3":5, "4":4, "5":5, "6":6, "7":3, "8":7, "9":6, "0":6}
    check = []

    n = int(input())

    print(getMin(n),getMax(n))
  
