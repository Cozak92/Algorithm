import collections
dp = [[True] + [False] * 10]

ax = collections.defaultdict(int)

res = 0

res += ax[3 - 7]

print(res)

ax[12] += 1

print(ax[12])