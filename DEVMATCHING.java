import java.util.Arrays;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.Queue;

public class DEVMATCHING {
    static class Pair {
        int x;
        int y;

        Pair(int x, int y) {
            this.x = x;
            this.y = y;
        }

        public int getY() {
            return y;
        }

        public int getX() {
            return x;
        }
    }


    private static HashMap<Character, Pair> condition = new HashMap<>();
    private static int endX;
    private static int endY;

    public static int solution(String[] drum) {

        condition.put('#', new Pair(1, 0));
        condition.put('>', new Pair(0, 1));
        condition.put('<', new Pair(0, -1));
        condition.put('*', new Pair(1, 0));


        //Character[][] field = makeTwoDe(drum);

        endX = drum.length;
        endY = drum[0].length();


        int answer = 0;
        for (int start = 0; start < endY; start++) {
            if(search(start, drum)){
                answer++;
            }
        }



        return answer;
    }


    public static boolean search(int start, String[] drum) {

        boolean[][] isVisited = new boolean[110][110];
        for(int i = 0; i < 110; i++){
            Arrays.fill(isVisited[i],false);
        }


        Queue<Pair> queue = new LinkedList<>();

        queue.add(new Pair(0, start));
        isVisited[0][start] = true;
        boolean isMet = false;

        while (!queue.isEmpty()) {
            Pair cur = queue.poll();
            int x = cur.getX();
            int y = cur.getY();
            Pair nextStep = condition.get(drum[x].charAt(y));

            int nx = x + nextStep.getX();
            int ny = y + nextStep.getY();

            if (nx >= endX) {
                return true;
            }
            if (!isVisited[nx][ny]) {

                if (drum[nx].charAt(ny) == '*') {
                    if (isMet) {
                        return false;
                    } else {
                        isMet = true;
                    }
                }
                isVisited[nx][ny] = true;
                queue.add(new Pair(nx, ny));
            }

        }
        return false;
    }


    public static void main(String[] args){
        String[] drum = {"######",">#*###","####*#","#<#>>#",">#*#*<","######"};
        System.out.println(solution(drum));
    }

}
