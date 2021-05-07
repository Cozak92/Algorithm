# import sys

# input = sys.stdin.readline


# H, W = map(int,list(input().split()))

# blocks = [[0 for _ in range(W)] for __ in range(H)]


# N = list(map(int,list(input().split())))
# i = 0

# for i in range(len(N)):
#     for j in range(N[i]):
# 	    blocks[j][i] = 1

# prev = 0
# result = 0

# # for block in blocks:
# #     print(block)

# for block in blocks:
#     flag = False
#     for x in range(W):
#         if block[x] == 1 and not flag:
#             if x + 1 < W:
#                 if block[x+1] == 0:
#                     prev = x

#                     flag = True
#         elif block[x] == 1 and flag:

#             result += abs(x - prev) -1
#             flag = False

# print(result)


import sys

input = sys.stdin.readline


H, W = map(int,list(input().split()))

blocks = list(map(int,list(input().split())))
left = 0
right = 0

result = 0

for i in range(1,len(blocks)):
    
    left, right = blocks[i], blocks[i] # 자신보다 높은 블록은 구해야된다고 왜 아무도 말 안해줌?

    # 자신을 기준으로 자신보다 높은 왼쪽,오른쪽 블록을 가져와서 둘중 낮은 블록의 해당 높이의 차이 만큼 뺴면 채워지는 물의 양이다.
    # 사이가 채워지는건줄 알았는데 자신의 머리위로 차는거였음 ㅋㅋ;
    
    for j in range(0,i):
        left = max(left,blocks[j])

    for k in range(i+1,W):
        right = max(right,blocks[k])


    MIN = min(left,right)

    result += (MIN - blocks[i])

print(result)
    
