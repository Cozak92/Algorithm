package Programmers;

import java.util.Arrays;
import java.util.HashMap;

public class 로또 {
    public int[] solution(int[] lottos, int[] win_nums) {
        HashMap<Integer,Integer> map = new HashMap<>();
        map.put(6,1);
        map.put(5,2);
        map.put(4,3);
        map.put(3,4);
        map.put(2,5);
        map.put(1,6);
        map.put(0,6);

        int win = 0;
        int joker = 0;
        for(int i = 0; i < lottos.length; i++){
            int finalI = i;
            if ( lottos[i] == 0 || Arrays.stream(win_nums).anyMatch(j -> j == lottos[finalI])){
                win++;
                joker = lottos[i] == 0 ? joker + 1 : joker;
            }
        }

        return new int[]{map.get(win), map.get(win-joker)};
    }
}
