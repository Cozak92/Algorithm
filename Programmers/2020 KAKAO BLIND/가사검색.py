def solution(words, queries):
    dictyo = {}
    answer = []
    q = "?"
    #접두사 접미사? 0= 접미사, 1 접두사
    for query in queries:
        cnt = query.count(q)
        temp = query
 
        while q in temp:
            print(cnt)
            temp = temp.replace(q,"")
        dictyo[temp] = [0,cnt]


    #?가 몇개인지?
    # LCS인데 접두사 접미사만, LCS가 아니라 다른 문자열 알고리즘?
    
    
    for query in dictyo:
        wordCnt = 0
       
        for word in words:
            
            if  query in word:
                print(word)
                print(query)
                LENG = len(query) + dictyo[query][1]                                                                                                         
                print(len(query))
                if LENG == len(word):
                    wordCnt += 1
                   
            # else:
            #     if word[0:len(query)] == query:
            #         
            #         wordCnt += 1
        answer.append(wordCnt)
                
                    
    
    return answer


words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]

print(solution(words,queries))