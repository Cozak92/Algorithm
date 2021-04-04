import collections


# 백준 1697번 - 숨바꼭질
# dx[0] = 1칸 뒤로, dx[1] = 1칸 앞으로 , dx[2] = 2*X

dx = [-1,1,2]

const = 100001

N, K = map(int, input().split())


def bfs(N,K):
    queue = collections.deque()
    cnt = [0]*const
    queue.append(N)

    if N > K:
        return N - K
       


    while queue:

        x = queue.popleft() 
        if x == K: # 큐 맨앞이 K까지 왔으면  더이상 탐색할 필요가 없음
            break;
        
        for i in range(len(dx)):            
            if i==2:
                nx = x * dx[i]
            else:
                nx = x + dx[i]
            if (0 <= nx < const) : # <= K 로 해놔서 인접한 노드 모든 경우가 탐색이 안됐음
                if cnt[nx] == 0 or ( cnt[x] + 1 < cnt[nx]):  # 방문한적 없거나 cnt[x] + 1 가 nx보다 작다는뜻은 더 빠를수 있다는 뜻이므로 갱신
                    cnt[nx] = cnt[x] + 1
                    #print("nx :",nx ,"x :", x)
                    #print("cnt[nx] : ", cnt[nx])
                    queue.append(nx)
            

    return cnt[K]


print(bfs(N,K))