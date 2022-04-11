package Baekjoon.사내스터디.`6주차`

import java.util.*

object Baekjoon15649 {
    lateinit var array: IntArray
    lateinit var isUsed: BooleanArray
    var m: Int = 0
    var n: Int = 0

    fun solve(k: Int){
        if(k == m){
            for(j in array){
                print("$j ")
            }
            println()
            return
        }

        for(i in 1..n){
            if(!isUsed[i]){
                isUsed[i] = true
                array[k] = i
                solve(k+1)
                isUsed[i] = false
            }
        }
    }

    @JvmStatic
    fun main(args: Array<String>){
        val sc = Scanner(System.`in`)
        n = sc.nextInt()
        m = sc.nextInt()
        array = IntArray(m)
        isUsed = BooleanArray(n + 1)

        solve(0)

    }
}