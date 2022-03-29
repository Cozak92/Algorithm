package Baekjoon.사내스터디.`5주차`

import java.util.*

object Baekjoon2630 {

    fun recursive(k: Int){



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