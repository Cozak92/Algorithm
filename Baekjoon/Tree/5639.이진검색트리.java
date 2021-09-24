package com.company;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

  private static class Node {
    int num;
    Node left, right;

    Node(int num) {
      this.num = num;
    }

    Node(int num, Node left, Node right) {
      this.num = num;
      this.left = left;
      this.right = right;
    }

    public void insert(int insertedNum) {

      if (insertedNum < this.num) {
        if (this.left == null) {
          this.left = new Node(insertedNum);
        } else {
          this.left.insert(insertedNum);
        }
      } else {
        if (this.right == null) {
          this.right = new Node(insertedNum);
        } else {
          this.right.insert(insertedNum);
        }
      }
    }
  }

  static void postOrder(Node node) {
    if (node.left != null) postOrder(node.left);
    if (node.right != null) postOrder(node.right);

    System.out.println(node.num);
  }

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    Node root = new Node(Integer.parseInt(br.readLine()));
    String input;
    while (true) {
      input = br.readLine();
      if (input == null || input.equals(""))
        break;
      root.insert(Integer.parseInt(input));
    }

    postOrder(root);

  }


}
