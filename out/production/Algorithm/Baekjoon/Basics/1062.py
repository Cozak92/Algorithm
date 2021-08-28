

basicLetters = ['a','n','t','i','c']

learnedLetters = 0

def dfs(start, N, K, lettersNum):
    global learnedLetters

    ret = 0

    if lettersNum == K :    

        for i in range(0,N):
            if wordCount[i] & learnedLetters == wordCount[i]: 
                ret += 1

            
        return ret


    for i in range(start,26):

        if (learnedLetters & (1 << i)) == 0:

            learnedLetters |= (1 << i)
            ret = max(ret,dfs(i + 1, N, K, lettersNum + 1))
            learnedLetters &= ~(1 << i)


    return ret

 

		
	
    



N, K = list(map(int,list(input().split())))




words = [[x for x in input().rstrip()[4:-4]] for _ in range(N)]
#print(words)
wordCount = [ 0  for _ in range(50)]
#print(wordCount)

for i in range(len(words)): 
    for j in range(len(words[i])): #배운 단어 체크
        wordCount[i] |= 1 << (ord(words[i][j]) - ord('a'))


learnedLetters |= 1 << (ord('a') - ord('a'));
learnedLetters |= 1 << (ord('n') - ord('a'))
learnedLetters |= 1 << (ord('c') - ord('a'))
learnedLetters |= 1 << (ord('t') - ord('a'))
learnedLetters |= 1 << (ord('i') - ord('a'))

if K < 5 or K == 26:
    print(N if K == 26 else 0) 
else:
    print(dfs(0,N,K,5))