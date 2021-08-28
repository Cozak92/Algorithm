l,c = list(map(int,input().split()))
vowel = ['a','e','i','o','u']
arr = list(input().split())
isUsed =[False for _ in range(c)]
password = ""
ans = 0
arr.sort()

def func(k,v,x,index):
    global ans
    global password
    if k == l:
        if v >= 1 and x >= 2:
            print(password)
        return

    prev = ""
    for i in range(index,c):
        if not isUsed[i] and arr[i] != prev:

            if arr[i] in vowel:
                isUsed[i] = True
                password += arr[i]
                prev = arr[i]
                func(k + 1, v + 1, x,i)
                password = password.replace(arr[i], "")
                isUsed[i] = False
            else:
                isUsed[i] = True
                password += arr[i]
                prev = arr[i]
                func(k + 1, v, x + 1 ,i)
                password = password.replace(arr[i], "")
                isUsed[i] = False

func(0,0,0,0)


    
