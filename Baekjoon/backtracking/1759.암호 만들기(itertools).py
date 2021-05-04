from itertools import combinations

l,c = list(map(int,input().split()))
vowel = ['a','e','i','o','u']
arr = list(input().split())
isUsed =[False for _ in range(c)]
password = ""
ans = 0
arr.sort()

pw = []

for item in combinations(arr,l):
    pw.append(item)

for p in pw:
    vowels = 0
    for letter in p:
  
        if letter in vowel:
            vowels += 1

    if vowels >= 1 and l - vowels >= 2:
        print("".join(p))
        



    
