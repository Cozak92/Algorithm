from collections import deque

n = int(input())

deck = deque([x for x in range(1,n+1)])
while len(deck) != 1:
    deck.popleft()
    t = deck.popleft()
    deck.append(t)

print(deck[0])
