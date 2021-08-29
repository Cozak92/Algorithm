package AtCoder.AtCoderBeginnerContest216;

import java.io.*;
import java.util.*;

public class Main {

  static int N;
  static int stoi(String s) { return Integer.parseInt(s);}
  static final int INF = 987654321;
  static HashSet<String> nameMap = new HashSet<>(1000);

  public void solve(){

  }

  public static void main(String args[]) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); //선언
    BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));//선언
    StringTokenizer st = new StringTokenizer(br.readLine());
    N = stoi(st.nextToken());

    for(int i = 0; i < N; i ++){
      String S = br.readLine();
      nameMap.add(S);
    }

    if(nameMap.size() == N){
      System.out.println("No");
    }
    else{
      System.out.println("Yes");
    }

    br.close();

  }


}