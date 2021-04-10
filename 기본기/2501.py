

N, K = map(int, list(input().split()))


count = 0

for i in range(1,N+1):
    if N % i == 0:
        count += 1
        if count == K:
            print(i)

print(0)