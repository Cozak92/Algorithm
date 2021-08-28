import sys


input = sys.stdin.readline

r1, c1, r2, c2 = list(map(int, list(input().split())))

max_level = max(abs(r1), abs(r2), abs(c1), abs(c2))

edges = [[r1,c1],[r1,c2],[r2,c2],[r2,c1]]

maxLevel = max(abs(r1),abs(r2),abs(c1),abs(c2))


for level in range(maxLevel-50,max_level+1):
    coord = [level,level]
    value = (level*2+1) ** 2

    for _ in range(level * 2):
        if r1<= coord[0] <= r2 and c1 <= coord[1] <= c2:
            result



