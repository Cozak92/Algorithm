import sys

N = int(input())
numbers = map(int,list(input().split()))
calculations = map(int,list(input().split()))

INF = sys.maxsize
MAX, MIN = 0
MAXResult, MINResult = -INF, INF

def calculating(index,calculations,numbers,calculation):

    if index == 0:
        return numbers[index],numbers[index]
    
    for i in range(4):
        if calculations[i] > 0:
            calculations[i] -= 1
            tempMAXResult, tempMINResult = calculating(index-1,calculations,numbers,calculation[i])
            if calculation == 0:
                MAXResult = max(MAXResult, tempMAXResult + numbers[index])
                MINResult = min(MINResult, tempMINResult + numbers[index])
            elif calculation == 1:
                MAXResult = max(MAXResult, tempMAXResult - numbers[index])
                MINResult = min(MINResult, tempMINResult - numbers[index])             
            elif calculation == 2:
                MAXResult = max(MAXResult, tempMAXResult * numbers[index])
                MINResult = min(MINResult, tempMINResult * numbers[index])
            elif calculation == 3:
                MAXResult = max(MAXResult, tempMAXResult // numbers[index])
                MINResult = min(MINResult, tempMINResult // numbers[index])

    return MAXResult,MINResult
    

calculating(index,calculating,numbers)
   




