# class Solution:
#     def halvesAreAlike(self, s: str) -> bool:
#         vowels  =['a','e','i','o','u']
#         lowerS = s.lower()
#         N = len(s)
#         print(N)
        
        
#         a = lowerS[:N//2]
#         b = lowerS[N//2:]
#         cntA, cntB = 0,0
        
#         for x in a:
#             if x in vowels:
#                 cntA += 1
#         for y in b:
#             if y in vowels:
#                 cntB += 1
                
#         if cntA == cntB:
#             return True
#         else:
#             return False


s='book'
vowels = 'aeiouAEIOU'
a = b = 0   
i, j = 0 , len(s) -1

while i < j:
    a += s[i] in vowels
    b += s[j] in vowels
    i += 1
    j -= 1
    print(a,b)

# return a == b
        