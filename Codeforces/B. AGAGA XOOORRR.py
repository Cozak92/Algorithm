import sys
from collections import Counter

input = sys.stdin.readline

t = int(input())

for _ in range(t):

    n = int(input())
    arr = list(map(int, list(input().split(" "))))

    countArr = Counter(arr).most_common()

    x, y = countArr[0]

    print(countArr)

    if y < 2:
        print("NO")
    else:
        print("YES")