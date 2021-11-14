package Baekjoon.DynamicPrograming;

import java.io.*;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class DanceDanceRevolution2342 {

    static ArrayList<Integer> tasks = new ArrayList<Integer>();
    static int[][][] dp = new int[5][5][100001];

    static int stoi(String s) {
        return Integer.parseInt(s);
    }

    static final int INF = 987654321;

    public static int move(int from, int to) {
        if (from == to) return 1;

        switch (from) {
            case 0:
                return 2;
            case 1:
                return to == 3 ? 4 : 3;
            case 2:
                return to == 4 ? 4 : 3;
            case 3:
                return to == 1 ? 4 : 3;
            case 4:
                return to == 2 ? 4 : 3;
        }
        return 0;
    }

    public static int solve(int l, int r, int n) {
        if (n == tasks.size()) return 0;

        if (dp[l][r][n] != 0) return dp[l][r][n];

        dp[l][r][n] = Math.min((move(l, tasks.get(n)) + solve(tasks.get(n), r, n + 1)), (move(r,tasks.get(n)) + solve(l, tasks.get(n), n + 1)));


        return dp[l][r][n];
    }

    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); //선언
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));//선언

        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = stoi(st.nextToken());
        while (n != 0) {
            System.out.println(n);
            tasks.add(n);
            n = stoi(st.nextToken());
        }

        System.out.println(solve(0, 0, 0));


        bw.flush();
        bw.close();
        br.close();

    }
}
