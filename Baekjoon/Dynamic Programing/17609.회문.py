import sys
input = sys.stdin.readline

t = int(input())

def isPalindrome(word,start,end):


    while start < end:
        #print(start, end)

        if word[start] == word[end]:
            start += 1
            end -= 1

        else: # 스킵구간
            leftCheck = isSmilar(word,start + 1, end)
            rightCheck = isSmilar(word,start, end - 1)

            if leftCheck or rightCheck:
                return 1
            else: return 2
    
    return 0

def isSmilar(word,start,end):

    while start < end:
        if word[start] == word[end]:
            start += 1
            end -= 1
        else: return False
    
    return True

for _ in range(t):
    word = list(input().rstrip())
    n = len(word)

    #print(n)

    print(isPalindrome(word,0,n-1))