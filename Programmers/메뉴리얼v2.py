from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []

    for k in course:
        candidates = []

        for order in orders:
            for food in combinations(order,k):

                temp = ''.join(sorted(food))
                candidates.append(temp)
        
        sortedCandidates = Counter(candidates).most_common()

        answer += [ menu for menu,cnt in sortedCandidates if cnt > 1 and cnt == sortedCandidates[0][1]]
