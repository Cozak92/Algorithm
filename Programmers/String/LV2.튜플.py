from collections import Counter

def solution(s):
    temp = s.replace("}","").replace("{","").split(",")
    return [int(x[0]) for x in Counter(temp).most_common()]