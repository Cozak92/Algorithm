import sys


S = sys.stdin.readline().rstrip()
P = sys.stdin.readline().rstrip()

print(S,P)

LEN = len(P)

start = 0
end = LEN

#print(start,end)

while end <= len(S):


    print(S[start:end])
    if S[start:end] == P:
        print(1)
        quit()
    else:
        start +=1
        end +=1

print(0)