# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    n = len(S)
    ans = 0
    arr = [0 for _ in range(n)]
    
    for i in range(n):
        if S[i] == "a":
            arr[i] += 1
    
    for i in range(n-1):
        arr[i + 1] += arr[i]
    for i in range(n-2):
        s = i + 1
        e = n - 1
        a = arr[i]
        while s < e:
            b = arr[s] - arr[i]
            c = arr[e] - arr[s]
            if a == b and b == c:
                ans += 1
            
            s += 1

            