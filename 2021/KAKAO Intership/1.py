from collections import defaultdict

dic = defaultdict(str)

#dic = {"zero" : "0", "one" : "1", "two": "2", "three": "3", "four" : "4", "five" : "5","six" :"6","seven" : "7","eight" : "8", "nine" : "9"}
alpha = ["zero", "one" , "two", "three", "four" , "five","six" ,"seven" ,"eight" , "nine"]
def solution(s):

    for i in range(10):
        dic[alpha[i]] = str(i)

    
    answer = 0
    temp =""
    string = ""
    for char in s:
        if char.isalpha() == False :
            temp += char
            
        else:
            string += char
        if dic[string] != "":
            temp += dic[string]
            string = ""
    

    return int(temp)
    

 

solution("one4seveneight")