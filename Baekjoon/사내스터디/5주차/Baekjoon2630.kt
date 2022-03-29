package Baekjoon.사내스터디.`5주차`

import java.util.*

object Baekjoon2630 {

    fun recursive(k: Int){
        // 왼쪽 0,0 ~ k/2, k/2
        // 오른쪽위 0,k/2 ~ k/2, k
        // 왼쪽아래 k/2,0 ~ k,k/2
        // 오른쪽아래 k/2,k/2 ~ k,k


    }

    @JvmStatic
    fun main(args: Array<String>) {
        val sc = Scanner(System.`in`)
        val n = sc.nextInt()
        val matrix = MutableList(n){ MutableList<Int>(n){0} }

        for(i in 0 until n){
            for(j in 0 until n){
                matrix[i][j] = sc.nextInt()
            }
        }

    }
}