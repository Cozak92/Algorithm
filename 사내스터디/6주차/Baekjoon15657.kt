package Baekjoon.사내스터디.`6주차`

object Baekjoon15657 {
    lateinit var array: IntArray
    lateinit var isUsed: BooleanArray
    lateinit var candidate: IntArray
    var sb = StringBuilder()


    fun solve(index: Int, k: Int, m: Int, n: Int) {
        if (k == m) {
            for (j in array) {
                sb.append("$j ")
            }
            sb.append("\n")
            return
        }

        for (i in 0 until n) {
            if(i >= index){
                array[k] = candidate[i]
                solve(i, k + 1, m, n)
            }

        }
    }


    @JvmStatic
    fun main(args: Array<String>) = with(System.`in`.bufferedReader()) {
        val (n, m) = readLine().split(" ").map { it.toInt() }
        candidate = readLine().split(" ").map { it.toInt() }.toIntArray()
        candidate.sort()
        array = IntArray(m)
        isUsed = BooleanArray(n + 1)
        solve(0, 0, m, n)
        println(sb);
    }
}