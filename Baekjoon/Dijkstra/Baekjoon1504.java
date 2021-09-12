package Baekjoon.Dijkstra;

import java.io.*;
import java.util.*;



public class Baekjoon1504 {
    static int stoi(String s) { return Integer.parseInt(s);}
    static final int INF = 987654321;
		static ArrayList<ArrayList<Node>> graph = new ArrayList<ArrayList<Node>>();
		static int N,E;

		static class Node implements Comparable<Node>{

			int index;
			int dist;

			public Node( int index, int dist){
				this.index = index;
				this.dist = dist;
			}

			public int compareTo(Node P){
				return this.dist - P.dist;
			}
		
		}
  
    public static int dijkstra(int start, int end){

			int[] dists = new int[N+1];
			Arrays.fill(dists, INF);
			PriorityQueue<Node> pq = new PriorityQueue<Node>();

			pq.add(new Node(start,0));
			dists[start] = 0;

			while(!pq.isEmpty()){

				Node curNode = pq.poll();

				
				if(dists[curNode.index] < curNode.dist) continue;

				for(Node nextNode : graph.get(curNode.index)){

					if(dists[nextNode.index] > nextNode.dist + curNode.dist){
						dists[nextNode.index] = nextNode.dist + curNode.dist;

						pq.add(new Node(nextNode.index, dists[nextNode.index]));
					}
				}
			}
			return dists[end];

    }
  
    public static void main(String args[]) throws IOException {
      BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); //선언
      BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));//선언
      StringTokenizer st = new StringTokenizer(br.readLine());
			N = stoi(st.nextToken());
			E = stoi(st.nextToken());

			int a,b,c;
			for(int i = 0; i <= N; i++){
				graph.add(new ArrayList<Node>());
			}

			for(int i = 0; i < E; i++){
				st = new StringTokenizer(br.readLine());
				a = stoi(st.nextToken());
				b = stoi(st.nextToken());
				c = stoi(st.nextToken());

				graph.get(a).add(new Node(b,c));
				graph.get(b).add(new Node(a,c));
			}
			st = new StringTokenizer(br.readLine());
			int v1 = stoi(st.nextToken());
			int v2 = stoi(st.nextToken());

			int ret = Math.min((dijkstra(1, v1) + dijkstra(v1, v2) + dijkstra(v2, N)) , dijkstra(1, v2) + dijkstra(v2, v1) + dijkstra(v1, N));

		
			System.out.println((ret < 0 || ret >= INF) ? -1 : ret);

      bw.flush();
      bw.close();
      br.close();
  
    }
}
