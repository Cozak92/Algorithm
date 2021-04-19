def solution(brown, yellow):
   
    total = brown + yellow
    for width in range(total,2,-1):

        if total % width == 0:

            height = total // width
            if yellow == (width - 2) * (height - 2):
                return [width,height]

solution(8,1)