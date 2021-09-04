package Baekjoon.math;

import java.io.*;
import java.util.*;

public class Baekjoon1629 {

    static int stoi(String s) { return Integer.parseInt(s);}
    static final int INF = 987654321;

    static long a,b,c;

    public static long pow(long A,long B){
        // System.out.println(a);
        // System.out.println(b);


        if(B == 1){
            return A % c;
        }

        long temp = pow(A, B / 2);
        if( B % 2 == 1){
            return (temp * temp % c) * A % c;
        }


        return temp * temp % c;
    }

    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); //선언
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));//선언
        StringTokenizer st = new StringTokenizer(br.readLine());
    
        a = stoi(st.nextToken());
        b = stoi(st.nextToken());
        c = stoi(st.nextToken());

        System.out.println(pow(a,b));
    
        bw.flush();
        bw.close();
        br.close();
    
      }
    
}
