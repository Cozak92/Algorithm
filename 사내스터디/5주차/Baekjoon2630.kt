package Baekjoon.사내스터디.`5주차`

import java.util.*

object Baekjoon2630 {

    lateinit var matrix: MutableList<MutableList<Int>>
    var white = 0
    var blue = 0

    fun recursive(x: Int, y: Int, size: Int) {
        // 왼쪽 0,0 ~ k/2, k/2
        // 오른쪽위 0,k/2 ~ k/2, k
        // 왼쪽아래 k/2,0 ~ k,k/2
        // 오른쪽아래 k/2,k/2 ~ k,k
        var sum = 0
        for (i in x until x + size) {
            for (j in y until y + size) {
                sum += matrix[i][j]
            }
        }

        if (sum == 0) {
            white++; return
        }
        if (sum == size * size) {
            blue++; return
        }

        recursive(x, y, size / 2)
        recursive(x + size / 2, y, size / 2)
        recursive(x, y + size / 2, size / 2)
        recursive(x + size / 2, y + size / 2, size / 2)

    }

    @JvmStatic
    fun main(args: Array<String>) {
        val sc = Scanner(System.`in`)
        val n = sc.nextInt()

        matrix = MutableList(n) { MutableList<Int>(n) { 0 } }
        for (i in 0 until n) {
            for (j in 0 until n) {
                matrix[i][j] = sc.nextInt()
            }
        }

        recursive(0, 0, n)

        println(white)
        println(blue)

        sc.close()
    }
}