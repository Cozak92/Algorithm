

t = int(input())

for i in range(t):
    a, b = list(map(int,input().split()))
    if b != 1:
        print("YES")
        print(a,a * b, a*(b+1))
    else:
        print("NO")

