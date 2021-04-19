from itertools import permutations

def solution(numbers):

    tempArr = set()

    for i in range(1,len(numbers)+1):
        for item in permutations(numbers,i):
            tempItem = int(''.join(list(item)))
            if tempItem == 1 or tempItem == 0:
                continue
            flag = True

            for j in range(2,tempItem):
                if tempItem % j == 0:
                    flag = False
                    break

            if flag:
                tempArr.add(tempItem)

    print(tempArr)

        
    answer = len(tempArr)
    return answer

solution("17")

