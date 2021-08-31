package AtCoder.AtCoderBeginnerContest216;

import java.io.*;
import java.util.*;

public class C {

  static int N;
  static int stoi(String s) { return Integer.parseInt(s);}
  static final int INF = 987654321;


  public static void main(String args[]) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); //선언
    BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));//선언
    StringTokenizer st = new StringTokenizer(br.readLine());
    N = stoi(st.nextToken());
    String ans = "";
    while (N != 0){
      if(N % 2 == 0){
        N /= 2;
        ans += "B";
      }
      else {
        N -= 1;
        ans += "A";
      }
    }
    StringBuffer sb = new StringBuffer(ans);
    String reversedStr = sb.reverse().toString();

    System.out.println(reversedStr);

    br.close();

  }


}