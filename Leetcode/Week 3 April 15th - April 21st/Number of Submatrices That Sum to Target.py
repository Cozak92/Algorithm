#https://meansoup.blogspot.com/2017/09/blog-post.html

from itertools import combinations
import collections


class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        row = len(matrix[0])
        columns = len(matrix)

        for r in matrix:
            for x in range(row - 1):
                r[x+1] += r[x] #각 row에 대한 누적합

        res = 0

        for start in range(row):
            for end in range(start,row):

                count = collections.defaultdict(int)
                current = 0
                count[0] = 1
                for column in range(columns):
                    current += matrix[column][end] - (matrix[column][start - 1] if start > 0 else 0)
                    res += count[current - target]
                    count[current] += 1

        #saved = [[0 for _ in range(len(matrix[0]))] for __ in range(len(matrix))]
        return res

       



       