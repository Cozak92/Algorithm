import java.io.*;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Baekjoon1238 {
    static int stoi(String s) {
        return Integer.parseInt(s);
    }

    static final int INF = 987654321;
    static int N, M, X;
    static ArrayList<ArrayList<Node>> list = new ArrayList<>();
    static ArrayList<ArrayList<Node>> revList = new ArrayList<>();
    static int[] dist;
    static int[] revDist;

    static class Node implements Comparable<Node> {
        int index;
        int distance;

        Node(int index, int distance) {
            this.index = index;
            this.distance = distance;
        }

        @Override
        public int compareTo(Node o) {
            return Integer.compare(this.distance, o.distance);
        }
    }

    static void init() {

        dist = new int[N + 1];
        revDist = new int[N + 1];

        Arrays.fill(dist, INF);
        Arrays.fill(revDist, INF);

        for (int i = 0; i <= N; i++) {
            list.add(new ArrayList<Node>());
            revList.add(new ArrayList<Node>());
        }
    }

    static void dijkstra(ArrayList<ArrayList<Node>> list, int start, int[] someDist) {
        PriorityQueue<Node> pq = new PriorityQueue<>();
        boolean[] check = new boolean[N + 1];

        someDist[start] = 0;
        pq.add(new Node(start, someDist[start]));

        while (!pq.isEmpty()) {
            Node curNode = pq.poll();
            int curDist = curNode.distance;
            int curIndex = curNode.index;

            if (curDist > someDist[curIndex]) continue;

            for (Node nextNode : list.get(curIndex)) {
                if (nextNode.distance + curDist < someDist[nextNode.index]) {
                    someDist[nextNode.index] = nextNode.distance + curDist;

                    pq.add(new Node(nextNode.index, someDist[nextNode.index]));
                }
            }
        }
    }

    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); //선언
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));//선언
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = stoi(st.nextToken());
        M = stoi(st.nextToken());
        X = stoi(st.nextToken());

        init();

        for (int i = 1; i <= M; i++) {
            st = new StringTokenizer(br.readLine());

            int v1 = stoi(st.nextToken());
            int v2 = stoi(st.nextToken());
            int dist = stoi(st.nextToken());

            list.get(v1).add(new Node(v2, dist));
            revList.get(v2).add(new Node(v1, dist));
        }

        dijkstra(list, X, dist);
        dijkstra(revList, X, revDist);

        int max = -1;
        for (int i = 1; i <= N; i++)
            max = Math.max(max, dist[i] + revDist[i]);
        System.out.println(max);

    }
}
