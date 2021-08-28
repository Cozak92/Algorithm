# **백준 5585**

def calculator(value):
    list = [500,100,50,10,5,1]
    cnt = 0;
    for i in list:
        while value // i > 0:
            value = value - i

            cnt += 1;


    return cnt
    
value = input()
value = int(value)
value = 1000 - value

print(calculator(value))