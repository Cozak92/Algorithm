package Baekjoon.사내스터디.`6주차`


object Baekjoon15652 {

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

        for (i in index until n) {
            if(!isUsed[i]){
                isUsed[i] = true
                array[k] = candidate[i]
                solve(i + 1, k + 1, m, n)
                isUsed[i] = false
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