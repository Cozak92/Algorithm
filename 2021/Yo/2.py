# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):

    month = {"Jan" : 1, "Feb" : 2, "Mar" : 3, "Apr": 4, "May" : 5, "Jun" : 6, "Jul" : 7, "Aug" : 8 , "Sep" : 9, "Oct" : 10 , "Nov" : 11 , "Dec" : 12 }
    size = 240 * (2 ** 10)
    ans = 0
    arr = S.split("\n")
    for s in arr:
        temp = s.strip().split(" ")
        if int(temp[0]) >= size and (int(temp[3]) >= int(1990) and month[temp[2]] >= 2):
            ans += 1



    return str(ans)

