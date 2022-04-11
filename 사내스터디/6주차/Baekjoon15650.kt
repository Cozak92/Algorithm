package Baekjoon.사내스터디.`6주차`

object Baekjoon15650 {

    lateinit var array: IntArray
    lateinit var isUsed: BooleanArray

    fun solve(index: Int, k: Int, m: Int, n: Int) {
        if (k == m) {
            for (j in array) {
                print("$j ")
            }
            println()
            return
        }

        for (i in index..n) {
            if (!isUsed[i]) {
                isUsed[i] = true
                array[k] = i
                solve(i + 1, k + 1, m, n)
                isUsed[i] = false
            }
        }
    }


    @JvmStatic
    fun main(args: Array<String>) = with(System.`in`.bufferedReader()) {
        val (n, m) = readLine().split(" ").map { it.toInt() }
        array = IntArray(m)
        isUsed = BooleanArray(n + 1)
        solve(1, 0, m, n)
    }
}