package Baekjoon.DynamicPrograming;

import java.io.*;
import java.util.StringTokenizer;

public class Baekjoon1932 {
    static int stoi(String s) {
        return Integer.parseInt(s);
    }

    static final int INF = 987654321;
    static int[][] arr = new int[505][505];
    static Integer[][] dp = new Integer[505][505];
    static int n;

    public static int solve(int step,int idx) {
        if (step == n) return dp[step][idx];

        if (dp[step][idx] != null) return dp[step][idx];

        dp[step][idx] = Math.max(solve(step + 1, idx), solve(step + 1, idx + 1)) + arr[step][idx];

        return dp[step][idx];
    }

    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); //선언
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));//선언
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = stoi(st.nextToken());

        for (int i = 1; i <= n; i++) {
            st = new StringTokenizer(br.readLine(), " ");
            for (int j = 1; j < i + 1; j++) {
                arr[i][j] = stoi(st.nextToken());
            }
        }

        for (int i = 1; i <= n; i++) {
            dp[n][i] = arr[n][i];
        }

        System.out.println(solve(1, 1));

    }
}
