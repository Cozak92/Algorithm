package Baekjoon.사내스터디.`6주차`

object Baekjoon15651 {

    lateinit var array: IntArray
    lateinit var isUsed: BooleanArray
    var sb = StringBuilder()


    fun solve( k: Int, m: Int, n: Int) {
        if (k == m) {
            for (j in array) {
                sb.append("$j ")
            }
            sb.append("\n")
            return
        }

        for (i in 1..n) {
            array[k] = i
            solve( k + 1, m, n)
        }
    }


    @JvmStatic
    fun main(args: Array<String>) = with(System.`in`.bufferedReader()) {
        val (n, m) = readLine().split(" ").map { it.toInt() }
        array = IntArray(m)
        isUsed = BooleanArray(n + 1)
        solve( 0, m, n)
        println(sb);
    }
}