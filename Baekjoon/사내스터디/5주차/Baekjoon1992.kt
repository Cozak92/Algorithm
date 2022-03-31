package Baekjoon.사내스터디.`5주차`

import java.util.*



object Baekjoon1992 {

    var n = 0
    var answer = ""
    lateinit var matrix: MutableList<MutableList<Int>>

    fun recursvie(x: Int, y: Int, size: Int){

        var sum = 0
        for (i in x until x + size) {
            for (j in y until y + size) {
                sum += matrix[i][j]
            }
        }
        if(sum == 0) {
            answer += "0"
            return
        }
        if( sum == size * size) {
            answer += "1"
            return
        }
        answer += "("

        recursvie(x,y,size/2)
        recursvie(x, y+ size/2, size/2)
        recursvie(x+ size/2,y, size/2)
        recursvie(x+size/2, y+size/2, size/2)
        answer += ")"
    }
    @JvmStatic
    fun main(args: Array<String>) {
        val sc = Scanner(System.`in`)
        n = sc.nextLine().toString().toInt()

        matrix = MutableList(n) { MutableList<Int>(n) { 0 } }

        for (i in 0 until n) {
            matrix[i] = sc.nextLine().map { it.toString().toInt() }.toMutableList()
        }

        recursvie(0,0,n)

        println(answer)
    }

}



