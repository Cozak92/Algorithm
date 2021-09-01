package Baekjoon.BFSAndDFS;

import java.io.*;
import java.util.*;


public class Baekjoon1325 {
  static int stoi(String s) { return Integer.parseInt(s);}
  static final int INF = 987654321;
	static int N,M;
	static Queue<Integer> q = new LinkedList<>();

	public static int bfs(int start,List<List<Integer>> arr){
		Boolean[] isVisited = new Boolean[N+1];
		Arrays.fill(isVisited,false);
		isVisited[start] = true;
		q.add(start);
		int hacked = 1;


		while(!q.isEmpty()){
			int cur = q.poll();
			
			for(int next : arr.get(cur) ){

				if(isVisited[next] != true){
					isVisited[next] = true;
					q.add(next);
					hacked++;

				}
			}
		}
		
		return hacked;
	}


  public static void main(String args[]) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); //선언
    BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));//선언
    StringTokenizer st = new StringTokenizer(br.readLine());
	N = stoi(st.nextToken());
	M = stoi(st.nextToken());
	List<List<Integer>> arr = new ArrayList<List<Integer>>(N);


	for(int i = 0; i <=N; i++){
		arr.add(new ArrayList<>());
	}
	for(int i = 0; i < M; i++){
		
		st = new StringTokenizer(br.readLine());
		int a = stoi(st.nextToken());
		int b = stoi(st.nextToken());

		
		arr.get(b).add(a);
	}

	int ret = Integer.MIN_VALUE;
	int[] cnt = new int[N+1];

	for(int i = 1; i <= N; i++){
		int temp = bfs(i,arr);
		ret = Math.max(ret,temp);
		cnt[i] = temp;
	}

	for(int i = 1; i <= N; i++){
		if(cnt[i] == ret){
			bw.write(i + " ");
		}
	}

    bw.flush();
    bw.close();
    br.close();
  }
}
