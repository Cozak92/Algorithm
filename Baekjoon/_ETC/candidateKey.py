from itertools import combinations

#재공부 https://wiselog.tistory.com/102

def solution(relation):
    answer = 0
    relationLen = len(relation)
    length = len(relation[0]) #속성 개수
    attr = [i for i in range(length)] #속성리스트(0~length-1)
    attrArr = []
    
    for i in range(length): #속성개수만큼
        com = list(combinations(attr, i+1)) #조합 리스트 구하기
        for j in range(len(com)): #조합 리스트의 각 조합별로 반복
            arr = []
            breaker = False
            for k in range(relationLen): #com 원소마다 relation 다 확인
                a = []
                for l in com[j]:
                    a.append(relation[k][l])
                if a not in arr:
                    arr.append(a)
                else:
                    breaker = True
                    break
            if not breaker:
                breaker2 = False
                for l in attrArr:
                    if set(com[j]).intersection(set(l)) == set(l):
                        breaker2 = True
                        break
                if not breaker2:
                    attrArr.append(com[j])
    #print(attrArr)
    return len(attrArr)