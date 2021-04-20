def solution(arr):
    answer = [0,0]

    def dfs(x,y,n):

        init = arr[x][y]

        for i in range(x,x+n): # x1,y1 x2,y2 이렇게 구하지말고 n개 만큼이동
            for j in range(y,y+n):

                if arr[i][j] != init: #하나라도 다르면 안된다.
                    half = n //2
                    dfs(x,y,half)
                    dfs(x+half,y,half)
                    dfs(x,y+half,half)
                    dfs(x+half,y+half,half)
                    return
        
        answer[init] += 1 #for문을 다돌았을때 init과 같다면 더 해줌
    
    dfs(0,0,len(arr))


    return answer
