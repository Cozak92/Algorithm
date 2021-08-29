package AtCoder.AtCoderBeginnerContest216;

import java.io.*;
import java.util.*;

public class poong {

    static int X,Y;
    static int stoi(String s) { return Integer.parseInt(s);}
    static final int INF = 987654321;

    public void solve(){

    }

    public static void main(String args[]) throws IOException {
      BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); //선언
      BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));//선언
      StringTokenizer st = new StringTokenizer(br.readLine(), ".");
      X = stoi(st.nextToken());
      Y = stoi(st.nextToken());
      System.out.println(X);
      if(0 <= Y && Y <= 2){
        System.out.println(X + "-");
      }
      else if(3 <= Y && Y <= 6){
        System.out.println(X);
      }
      else if(7 <= Y && Y <= 9){
        System.out.println(X + "+");
      }

      bw.flush();
      bw.close();
      br.close();

    }


}
