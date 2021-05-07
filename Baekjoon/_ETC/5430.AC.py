t = int(input())


for _ in range(t):
    order = input()

    rCnt = order.count("R")
    dCnt = len(order) - rCnt

    n = int(input())

    if dCnt > n:
        print("error")

    arr = input()
    if arr == []:
        print("error")
    arr = arr[1:len(arr)-1]
    arr = arr.split(",")
    cnt = 0
    counter
    for j in range(len(order)):
        if arr[j] == "R":
            cnt += 1
        else:
