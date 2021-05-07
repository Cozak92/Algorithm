alpha='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers='32123333113133122212112221'
cnt=0
s=input()
for i in range(len(s)):
   cnt+=int (numbers[alpha.index(s[i])])
   cnt%=10
if cnt%2==0: print("You're the winner?")
else: print("I'm a winner!")