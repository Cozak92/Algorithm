import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))
arr.sort()
ret = sys.maxsize
for i in range(n-2):

    s = i + 1
    e = n - 1
    
    while s < e:
        
        temp = arr[i] + arr[s] + arr[e]
        if abs(temp) < ret:
            ret = abs(temp)
            index1 = i
            index2 = s
            index3 = e
        
    
        if temp < 0:
            s += 1
        elif temp > 0:
            e -= 1
        else:
            print(arr[index1],arr[index2],arr[index3])
            exit(0)

print(arr[index1],arr[index2],arr[index3])
