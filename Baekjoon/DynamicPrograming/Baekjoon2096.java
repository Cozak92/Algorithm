package Baekjoon.DynamicPrograming;

import java.io.*;
import java.util.*;


public class Baekjoon2096 {
  static int stoi(String s) { return Integer.parseInt(s);}
  static final int INF = 987654321;


  public static void main(String args[]) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); //선언
    BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));//선언
    StringTokenizer st = new StringTokenizer(br.readLine());
  
    int N = stoi(st.nextToken());
    int[][] arr = new int[N+1][4];

    for(int i = 1; i <= N; i++){
      st = new StringTokenizer(br.readLine());
      
      for(int j = 1; j < 4; j++){

        arr[i][j] = stoi(st.nextToken());
      }
      
    }
    int[][] max = new int[N+1][4];
    int[][] min = new int[N+1][4];

    for (int i = 1; i <= N; i++) {
      max[i][1] += Math.max(max[i-1][1], max[i-1][2]) + arr[i][1];
      max[i][2] += Math.max(Math.max(max[i-1][1], max[i-1][2]), max[i-1][3]) + arr[i][2];
      max[i][3] += Math.max(max[i-1][2], max[i-1][3]) + arr[i][3];
      
      min[i][1] += Math.min(min[i-1][1], min[i-1][2]) + arr[i][1];
      min[i][2] += Math.min(Math.min(min[i-1][1], min[i-1][2]), min[i-1][3]) + arr[i][2];
      min[i][3] += Math.min(min[i-1][2], min[i-1][3]) + arr[i][3];
    }

    int maxValue = 0, minValue = Integer.MAX_VALUE;
    for(int i=1; i<=3; i++) {
        maxValue = Math.max(maxValue, max[N][i]);
        minValue = Math.min(minValue, min[N][i]);
    }

    bw.write(maxValue + " " + minValue );

    bw.flush();
    bw.close();
    br.close();

  }
}
