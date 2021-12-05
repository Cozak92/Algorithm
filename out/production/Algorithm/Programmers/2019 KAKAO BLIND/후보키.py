

# def solution(relation):
#     column = len(relation)
#     row = len(relation[0])
#     answer = 0

#     checkDuple = [set() for _ in range(row)]
#     print(checkDuple)
    
#     for j in range(row):
#         for i in range(column):
#             checkDuple[j].add(relation[i][j])
#     print(checkDuple)

#     candidate = []
#     Cancandidate = []

#     for i in range(row):
#         if len(checkDuple[i]) < column:
#             Cancandidate.append(i)
#         else:
#             answer += 1
#             print(answer)
        
#     for item in combinations(Cancandidate,2):
#         x1, x2 = item
        
#         flag = True
#         for k in candidate:
#             if x1 in k or x2 in k:
#                 flag = False
#         if flag:
#             candidate.append(item)


   
#     return answer + len(candidate)

from itertools import combinations  





def solution(relation):
    column = len(relation)
    row = len(relation[0])

    subset = []
    # 1단계. 모든 부분 집합 구하기
    for j in range(1,row+1):
        for item in combinations(range(row), j):
            subset.append(list(item))
    
    candidate = []

    # 2단계. 부분 집합 중 유일성 체크

    for k in range(len(subset)):
        findOnly = set()

        for j in range(column):

            row = ""

            for i in range(len(subset[k])):

                row += str(relation[j][subset[k][i]])

            findOnly.add(row)
                  

        if len(findOnly) == column:

            candidate.append(subset[k])


    # 3단계. 부분 집합 중 최소성 체크
    # 길이 순으로 정렬해야되나? 어차피 낮은게 앞으로 올텐데..

    realCandidate = []

    for c in candidate:
        c = set(c)
        flag = True
        for x in realCandidate:
            if x.issubset(c):
                flag = False
        if flag:
            realCandidate.append(c)

            



    return len(realCandidate)

    
    







relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]

print(solution(relation))