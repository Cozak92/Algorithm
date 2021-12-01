package Programmers.Impl.programmers;

public class rotateMatrix {
    public static int[] solution(int rows, int columns, int[][] queries) {
        int[] answer = new int[queries.length];
        int[][] matrix = new int[rows + 1][columns + 1];
        int index = 1;
        for (int i = 1; i <= rows; i++) {
            for (int j = 1; j <= columns; j++) {
                matrix[i][j] = index++;
            }
        }

        for (int i = 1; i <= rows; i++) {
            for (int j = 1; j <= columns; j++) {
                System.out.print(matrix[i][j] + " ");
            }
            System.out.println();
        }

        for (int i = 0; i < queries.length; i++) {
            int startX = queries[i][0];
            int startY = queries[i][1];

            int endX = queries[i][2];
            int endY = queries[i][3];

            int basket = matrix[startX][startY];

            int tmp = matrix[startX][startY];
            for (int x = startX + 1; x <= endX; x++) {
                basket = Math.min(matrix[x][startY], basket);
                matrix[x - 1][startY] = matrix[x][startY];
            }
            for (int y = startY + 1; y <= endY; y++) {
                basket = Math.min(matrix[endX][y], basket);
                matrix[endX][y - 1] = matrix[endX][y];
            }
            for (int x = endX - 1; x >= startX; x-- ){
                basket = Math.min(matrix[x][endY], basket);
                matrix[x + 1][endY] = matrix[x][endY];
            }
            for (int y = endY - 1; y > startY; y--) {
                basket = Math.min(matrix[startX][y], basket);
                matrix[startX][y + 1] = matrix[startX][y];
            }

            matrix[startX][startY + 1] = tmp;

            answer[i] = basket;
        }
        return answer;
    }

    public static void main(String args[]) {
        int[][] queries = {{2, 2, 5, 4}, {3, 3, 6, 6}, {5, 1, 6, 3}};
        int[] answer = solution(6, 6, queries);

        for (int a : answer) {
            System.out.println(a);
        }
    }
}
