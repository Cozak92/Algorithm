class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        n = len(matrix)

        for i in range(n//2 + n % 2): # i = 각 층,레벨; 나머지를 더하는 이유는 홀수일 경우 가운데 열까지 가야하므로
            for j in range(n//2): # 움직이는 축

                temp = matrix[i][j]
                #print(matrix[i][j])
                matrix[i][j] = matrix[n - j - 1][i]
                #print(matrix[n - j - 1][i])
                matrix[n - j - 1][i] = matrix[n - i - 1][n - j - 1]
                #print(matrix[n - j - 1][n - i - 1])
                matrix[n - i - 1][n - j - 1] = matrix[j][n - i - 1]
                #print(matrix[j][n - i - 1])
                matrix[j][n - i - 1] = temp