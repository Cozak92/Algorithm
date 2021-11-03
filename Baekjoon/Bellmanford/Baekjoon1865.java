package Baekjoon.Bellmanford;

import AtCoder.AtCoderBeginnerContest216.A;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Baekjoon1865 {


    static class Pair {
        private final int x;
        private final int y;

        Pair(int x, int y) {
            this.x = x;
            this.y = y;
        }

        public int getX() {
            return x;
        }

        public int getY() {
            return y;
        }
    }

    static ArrayList<Integer> dist = new ArrayList<>();
    static ArrayList<Pair>[] v = (ArrayList<Pair>[]) new ArrayList[502];
    static final int INF = 987654321;

    static int stoi(String s) {
        return Integer.parseInt(s);
    }

    static boolean bellman(int N) {
        dist.set(1, 0);
        boolean update = false;
        for (int j = 1; j < N; j++) {
            update = false;
            for (int k = 1; k <= N; k++) {
                for (Pair p : v[k]) {
                    if (dist.get(p.getX()) > p.getY() + dist.get(k)) {
                        dist.set(p.getX(), p.getY() + dist.get(k));
                        update = true;
                    }

                }
            }
            if (!update) {
                break;
            }
        }
        if (update) {
            for (int i = 1; i <= N; i++) {
                for (Pair p : v[i]) {
                    if (dist.get(p.getX()) > p.getY() + dist.get(i)) {
                        return true;
                    }

                }
            }
        }
        return false;
    }


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        for (int j = 0; j < 502; j++) {
            dist.add(INF);
        }


        int n = stoi(st.nextToken());

        for (int i = 0; i < n; i++) {
            int N, M, W;
            st = new StringTokenizer(br.readLine());

            N = stoi(st.nextToken());
            M = stoi(st.nextToken());
            W = stoi(st.nextToken());
            for (int j = 0; j <= N; j++) {
                v[j] = (new ArrayList<>());
            }

            for (int j = 0; j < M + W; j++) {
                st = new StringTokenizer(br.readLine());
                int s = stoi(st.nextToken());
                int e = stoi(st.nextToken());
                int t = stoi(st.nextToken());

                if (j < M) {
                    v[s].add(new Pair(e, t));
                    v[e].add(new Pair(s, t));
                } else {
                    v[s].add(new Pair(e, -t));
                }

            }


            System.out.println(bellman(N) ? "YES" : "NO");

        }


    }
}
