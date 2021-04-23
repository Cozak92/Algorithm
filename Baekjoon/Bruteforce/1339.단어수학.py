from collections import defaultdict

n = int(input())
posTable = defaultdict(int)
apha = ["9","8","7","6","5","4","3","2","1","0"]

words = []

for i in range(n):

    word = input()
    words.append(word)
    k = 0
    for l in word:

        posTable[l] += 10 ** ((len(word) - k)-1)  * 9
        k += 1



posTable = sorted(posTable.items(), key = lambda x : x[1],reverse = True)

i = 0
for alphabet in posTable:
   


    for j in range(len(words)):

        while alphabet[0] in words[j]:

            words[j] = words[j].replace(alphabet[0],apha[i])

    

    i += 1


SUM = 0
for word in words:
    SUM += int(word)
print(SUM)