import sys

input = sys.stdin.readline

bottles, targetBottles = list(map(int, list(input().split())))



answer = 0




def sol(bottles):
    count = 0


    while 1:
        #print(bottles)
    
        spareBottles = bottles % 2
        tempBottles = bottles // 2
        
        
        count += spareBottles
        bottles = tempBottles


        if bottles ==0:
            break

    return count

n = bottles

#print(bottles)

if bottles<= targetBottles:
    print(0)
else:
    while True:
        if sol(n) <= targetBottles:
            print(n-bottles)
            break
        else:
            n += 1
            print(n)

    



