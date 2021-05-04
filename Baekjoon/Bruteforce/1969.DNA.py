from collections import defaultdict

n, m = list(map(int,list(input().split())))
count = defaultdict(int)
dna = [input() for _ in range(n)]

ansString = ""
ans = 0
for i in range(m):
    count = defaultdict(int)
    arr = []
    MAX = -1
    char = ""
    for j in range(n):
        count[dna[j][i]] += 1
    for k,v in count.items():
        if MAX < v:
            MAX = v
            char = k
        elif MAX == v:
            arr.append(char)
            arr.append(k)
            char = sorted(arr)[0]
    ans += (n - MAX)
    ansString += char
print(ansString)
print(ans)



