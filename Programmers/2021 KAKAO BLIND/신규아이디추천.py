import string
def solution(new_id):
    answer = ''
    checkList = ''
    lowercase = string.ascii_lowercase
    digits = string.digits
    checkList = checkList + lowercase
    checkList = checkList + digits
    checkList += '-_.'

    print(checkList) 
    #1단계
    new_id = new_id.lower()

    #2단계
    for word in new_id:
        if word not in checkList:
            print(word)
            new_id = new_id.replace(word,"")
    
    # new_id = new_id.replace((letter for letter in new_id if letter not in checkList ),'')
    
    #3단계
    while '..' in new_id:
        new_id = new_id.replace('..', '.')

    #4단계

    new_id = new_id[1:] if new_id[0] == '.' and len(new_id) > 1 else new_id
    new_id = new_id[:-1] if new_id[-1] == '.' else new_id

    new_id = 'a' if new_id == '' else new_id

    if len(new_id) >= 16:
        new_id = new_id[:15]

        if new_id[-1] == '.':
            new_id = new_id[:-1]
            
    while len(new_id) <= 2:
        new_id += new_id[-1]
        
    

    print(new_id)

    return new_id




new_id = 	"1234"
print(new_id.isascii())
solution(new_id)