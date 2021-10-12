package Programmers.WeeklyChallenge;

import java.util.*;

public class Weekly8 {
    public static int solution(int[][] sizes) {

        int length = sizes.length;
        ArrayList<Integer> width = new ArrayList<>();
        ArrayList<Integer> height = new ArrayList<>();
        for(int[] size : sizes){
            Arrays.sort(size);
            width.add(size[0]);
            height.add(size[1]);
        }
        int Wmax = Collections.max(width);
        int Hmax = Collections.max(height);

        return Wmax * Hmax;
    }

    public static void main(String[] args) {
        int[][] sizes = {{60, 50}, {30, 70}, {60, 30}, {80, 40}};
        System.out.println(solution(sizes));
    }
}

/* 다른사람 풀이 */
//import java.util.*;
//class Solution {
//    public int solution(int[][] sizes) {
//        return Arrays.stream(sizes).reduce((a, b) -> new int[]{
//                Math.max(Math.max(a[0], a[1]), Math.max(b[0], b[1])), Math.max(Math.min(a[0], a[1]), Math.min(b[0], b[1]))
//        }).map(it -> it[0] * it[1]).get();
//    }
//}

