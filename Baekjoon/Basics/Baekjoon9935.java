package Baekjoon.Basics;

import java.io.*;
import java.util.ArrayList;
import java.util.Stack;
import java.util.StringTokenizer;

public class Baekjoon9935 {

    static int stoi(String s) {
        return Integer.parseInt(s);
    }

    static final int INF = 987654321;

    public void solve() {

    }

    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); //선언
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));//선언

        String ori = br.readLine();
        String bomb = br.readLine();
        Stack<Character> stack = new Stack<>();

        for (int i = 0; i < ori.length(); i++) {
            stack.push(ori.charAt(i));
            if (stack.size() < bomb.length()) continue;

            boolean detected = true;

            for (int j = 0; j < bomb.length(); j++){
                if(stack.get(stack.size() - bomb.length() + j) != bomb.charAt(j)){
                    detected = false;
                    break;
                }
            }

            if(detected){
                for(int j = 0; j < bomb.length(); j++){
                    stack.pop();
                }
            }
        }

        StringBuilder sb = new StringBuilder();
        for(Character ch : stack) {
            sb.append(ch);
        }

        System.out.println(sb.length() > 0 ? sb.toString() : "FRULA");


        bw.flush();
        bw.close();
        br.close();

    }
}
