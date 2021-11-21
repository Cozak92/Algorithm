package Baekjoon;

import java.io.*;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Baekjoon11404 {
    static int stoi(String s) {
        return Integer.parseInt(s);
    }

    static final int INF = 987654321;
    static int N;
    static int M;
    static int[][] graph;


    public static void solve() {

        for (int mid = 1; mid <= N; mid++) {
            for (int start = 1; start <= N; start++) {
                for (int end = 1; end <= N; end++) {
                    graph[start][end] = Math.min(graph[start][end], graph[start][mid] + graph[mid][end]);
                }
            }
        }

    }

    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); //선언
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));//선언
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = stoi(st.nextToken());
        st = new StringTokenizer((br.readLine()));
        M = stoi(st.nextToken());

        graph = new int[N + 1][N + 1];

        for (int i = 1; i <= N; i++) {
            for(int j =1; j <=N; j++){
                if(i == j) continue;
                graph[i][j] = INF;
            }
        }


        for (int i = 0; i < M; i++) {
            st = new StringTokenizer((br.readLine()));
            int a = stoi(st.nextToken());
            int b = stoi(st.nextToken());
            int c = stoi(st.nextToken());
            graph[a][b] = Math.min(graph[a][b], c);
        }
        solve();

        for(int i = 1; i <= N; i++){
            for(int j = 1 ; j <= N; j++){
                System.out.print(graph[i][j] == INF ? 0 + " " : graph[i][j] + " ");
            }
            System.out.println();
        }


        bw.flush();
        bw.close();
        br.close();

    }
}
