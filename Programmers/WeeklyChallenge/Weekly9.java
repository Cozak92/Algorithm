package Programmers.WeeklyChallenge;



import AtCoder.AtCoderBeginnerContest216.A;

import java.util.*;

class Weekly9 {

    ArrayList<ArrayList<Integer>> tree = new ArrayList<>();


    public int find(int[] parent, int x){
        if(parent[x] == x){
            return x;
        }
        parent[x] = find(parent,parent[x]);
        return parent[x];
    }

    public void union(int[] parent, int x, int y){
        int X = find(parent, x);
        int Y = find(parent, y);

        if(X < Y){
            parent[Y] = X;
        } else {
            parent[X] = Y;
        }
    }

    public int solution(int n, int[][] wires) {

        ArrayList<Integer> answers = new ArrayList<>();
        for(int i = 0; i < n; i++){
            int[] parent = new int[n+1];

            for(int q = 1; q <= n; q++){
                parent[q] = q;
            }

            for(int j = 0; j < n; j++){
                if(i == j) continue;
                int x = wires[j][0];
                int y = wires[j][1];

                union(parent,x,y);
            }
            for(int m = 1; m <= n; m++){
                find(parent,m);
            }

            int count = 0;
            for(int k = 1; k <= n; k++){
                if(parent[k] == 1){
                    count++;
                }
            }
            int temp = n - count;

            answers.add(Math.abs(count - temp));
        }

        return Collections.min(answers);
    }
}