

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

  static class Pair {
    private int x, y;

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

  static int[] dy = {0, 1, -1, 0};
  static int[] dx = {1, 0, 0, -1};
  static int[][] board = new int[110][110];
  static boolean[][] air = new boolean[110][110];
  static final int INF = 987654321;
  static int N, M;

  static int stoi(String s) {
    return Integer.parseInt(s);
  }

  static void checkAir() {
    boolean[][] isVisited = new boolean[110][110];

    for (boolean c[] : isVisited) {
      Arrays.fill(c, false);
    }

    Queue<Pair> q = new LinkedList<>();
    isVisited[0][0] = true;
    q.add(new Pair(0, 0));

    while (!q.isEmpty()) {
      Pair temp = q.poll();

      for (int i = 0; i < 4; i++) {
        int nx = temp.getX() + dx[i];
        int ny = temp.getY() + dy[i];

        if ((0 > nx || nx >= N) || (0 > ny || ny >= M)) continue;
        if (isVisited[nx][ny]) continue;
        if (board[nx][ny] != 0) continue;
        isVisited[nx][ny] = true;
        air[nx][ny] = true;
        q.add(new Pair(nx, ny));
      }
    }
  }

  static int simulation() {
    int times = 0;

    while (true) {

      boolean flag = false;
      checkAir();
      canMelted();

      for(int i = 0; i < N; i++){
        for(int j = 0; j < M; j++){
          if(board[i][j] == -1) board[i][j] = 0;
          if(board[i][j] == 1) flag = true;
        }
      }
      times++;

      if(!flag) break;
    }
    return times;
  }

  private static void canMelted() {
    for (int i = 0; i < N; i++) {
      for (int j = 0; j < M; j++) {

        if(board[i][j] == 1){
          int cnt = 0;

          for(int k = 0; k < 4; k++){
            int nx = i + dx[k];
            int ny = j + dy[k];

            if ((0 > nx || nx >= N) || (0 > ny || ny >= M)) continue;
            if (!air[nx][ny]) continue;

            cnt++;


          }

          if(cnt >= 2) board[i][j] = -1;
        }
      }
    }
  }

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());
    N = stoi(st.nextToken());
    M = stoi(st.nextToken());

    for (boolean a[] : air) {
      Arrays.fill(a, false);
    }

    air[0][0] = true;

    for (int i = 0; i < N; i++) {
      st = new StringTokenizer(br.readLine());

      for (int j = 0; j < M; j++) {
        board[i][j] = stoi(st.nextToken());

      }
    }


    System.out.println(simulation());

  }

}


